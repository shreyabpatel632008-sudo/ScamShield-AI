import streamlit as st

st.set_page_config(
    page_title="ScamShield AI",
    page_icon="🛡️",
    layout="wide"
)

# -----------------------------
# Custom Styling
# -----------------------------
st.markdown("""
<style>
    .hero {
        padding: 2rem 2rem 1.5rem 2rem;
        border-radius: 18px;
        background: linear-gradient(135deg, #f8fafc, #eef2ff);
        border: 1px solid #e2e8f0;
        margin-bottom: 1.5rem;
    }

    .hero h1 {
        margin-bottom: 0.3rem;
        font-size: 2.5rem;
    }

    .hero p {
        font-size: 1.1rem;
        color: #475569;
        margin-bottom: 0;
    }

    .section-title {
        font-size: 1.35rem;
        font-weight: 700;
        margin-top: 1.5rem;
        margin-bottom: 0.8rem;
    }

    .risk-card {
        padding: 1.1rem;
        border-radius: 14px;
        border: 1px solid #fecaca;
        background: #fff7f7;
        margin-bottom: 0.8rem;
    }

    .risk-card h4 {
        margin: 0 0 0.4rem 0;
    }

    .evidence {
        font-size: 0.9rem;
        color: #7f1d1d;
        margin-bottom: 0.4rem;
    }

    .safe-card {
        padding: 1.2rem;
        border-radius: 14px;
        border: 1px solid #bbf7d0;
        background: #f0fdf4;
        margin-top: 1rem;
    }

    .safe-card h4 {
        margin-top: 0;
    }

    .step {
        margin: 0.55rem 0;
    }

    .footer-note {
        text-align: center;
        color: #64748b;
        font-size: 0.85rem;
        margin-top: 2rem;
        padding-top: 1rem;
        border-top: 1px solid #e2e8f0;
    }
</style>
""", unsafe_allow_html=True)


# -----------------------------
# Scam Detection Logic
# -----------------------------
def analyze_message(text):
    text_lower = text.lower()

    categories = []

    checks = [
        (
            "Urgent language",
            [
                "urgent",
                "immediately",
                "act now",
                "within 24 hours",
                "last chance"
            ],
            "Pressure to act immediately can discourage users from taking time to verify a request.",
            "Pressure tactics are commonly used to make people act before they have time to check the information."
        ),
        (
            "Payment request",
            [
                "pay",
                "payment",
                "fee",
                "registration fee",
                "processing fee",
                "deposit"
            ],
            "Unexpected fees or requests for money should be independently verified before making any payment.",
            "Requests for money can create financial risk, especially when the organization or offer has not been independently verified."
        ),
        (
            "Credential request",
            [
                "password",
                "otp",
                "one time password",
                "pin",
                "cvv"
            ],
            "Sensitive information such as OTPs, passwords, PINs, or CVVs should not normally be shared with unknown people or services.",
            "Sensitive credentials can be misused to access accounts or authorize transactions."
        ),
        (
            "Suspicious link/action",
            [
                "click this link",
                "click here",
                "verify your account",
                "open this link"
            ],
            "Links asking you to verify or claim something should be checked carefully and preferably accessed through an official website.",
            "Unexpected links can lead to fake websites or pages designed to collect personal information."
        ),
        (
            "Prize or reward claim",
            [
                "you have won",
                "winner",
                "congratulations",
                "selected",
                "claim your reward",
                "free reward"
            ],
            "Unexpected prizes or rewards can be used to persuade users to click links, provide information, or make payments.",
            "Unexpected rewards may be used as bait to encourage risky actions."
        )
    ]

    for name, indicators, explanation, concern in checks:
        found = [item for item in indicators if item in text_lower]

        if found:
            categories.append({
                "name": name,
                "indicators": found,
                "explanation": explanation,
                "concern": concern
            })

    return categories


# -----------------------------
# Header
# -----------------------------
st.markdown("""
<div class="hero">
    <h1>🛡️ ScamShield AI</h1>
    <p>Understand the red flags before you take the risk.</p>
</div>
""", unsafe_allow_html=True)


st.markdown(
    "Paste a suspicious message, job offer, scholarship message, email, "
    "or payment request. ScamShield will help identify potential warning "
    "signs and suggest safer next steps."
)


# -----------------------------
# Analyzer
# -----------------------------
st.markdown(
    '<div class="section-title">🔎 Analyze a Message</div>',
    unsafe_allow_html=True
)

message = st.text_area(
    "Paste the message you want to check:",
    height=190,
    placeholder=(
        "Example: Congratulations! You have been selected for a scholarship. "
        "Pay a registration fee immediately and provide your OTP..."
    ),
    label_visibility="collapsed"
)

analyze_button = st.button(
    "🔍 Analyze Message",
    type="primary",
    use_container_width=True
)


# -----------------------------
# Results
# -----------------------------
if analyze_button:

    if not message.strip():
        st.warning("Please paste a message before analyzing it.")

    else:
        results = analyze_message(message)

        st.markdown(
            '<div class="section-title">📊 Analysis Result</div>',
            unsafe_allow_html=True
        )

        if results:

            count = len(results)

            st.error(
                f"⚠️ ScamShield identified **{count} potential warning area(s)**."
            )

            st.markdown(
                '<div class="section-title">⚠️ Potential Warning Signs</div>',
                unsafe_allow_html=True
            )

            for result in results:

                evidence = ", ".join(
                    f"`{item}`" for item in result["indicators"]
                )

                st.markdown(
                    f"""
                    <div class="risk-card">
                        <h4>⚠️ {result["name"]}</h4>
                        <div class="evidence">
                            Detected indicators: {evidence}
                        </div>
                        <div>
                            {result["concern"]}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            st.markdown(
                '<div class="section-title">💡 Why These May Be Concerning</div>',
                unsafe_allow_html=True
            )

            for result in results:
                st.markdown(
                    f"**{result['name']}** — {result['explanation']}"
                )

            

        else:

            st.success(
                "✅ No common warning indicators were detected in this message."
            )

            st.info(
                "This does not guarantee that the message is safe. "
                "Always verify important requests through trusted official sources."
            )


# -----------------------------
# Disclaimer
# -----------------------------
st.markdown('<div class="section-title">🛡️ Safer Next Steps</div>', unsafe_allow_html=True)

st.success(
    "✓ Do not send money until the request has been independently verified."
)

st.success(
    "✓ Do not share OTPs, passwords, PINs, CVVs, or other sensitive information."
)

st.success(
    "✓ Avoid clicking suspicious links."
)

st.success(
    "✓ Verify the organization using its official website or trusted contact details."
)

st.success(
    "✓ If the message claims to be from a company, contact that company through an independently verified channel."
)