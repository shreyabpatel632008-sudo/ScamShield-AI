import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="ScamShield AI",
    page_icon="🛡️",
    layout="wide"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>
    .main {
        background-color: #f7f9fc;
    }

    .hero {
        padding: 25px 10px 15px 10px;
    }

    .hero h1 {
        font-size: 42px;
        margin-bottom: 5px;
    }

    .hero p {
        font-size: 18px;
        color: #5f6b7a;
    }

    .result-card {
        padding: 20px;
        border-radius: 14px;
        background-color: white;
        border: 1px solid #e5e7eb;
        margin-top: 15px;
    }

    .warning-item {
        padding: 10px;
        margin: 7px 0;
        border-radius: 8px;
        background-color: #fff7ed;
        border-left: 4px solid #f97316;
    }

    .safe-item {
        padding: 10px;
        margin: 7px 0;
        border-radius: 8px;
        background-color: #f0fdf4;
        border-left: 4px solid #22c55e;
    }

    .disclaimer {
        font-size: 13px;
        color: #6b7280;
        padding-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.markdown("""
<div class="hero">
    <h1>🛡️ ScamShield AI</h1>
    <p>Understand the red flags before you take the risk.</p>
</div>
""", unsafe_allow_html=True)

st.info(
    "Paste a suspicious message, job offer, scholarship message, "
    "email, or payment request. ScamShield will help identify "
    "potential warning signs and suggest safer next steps."
)

# -----------------------------
# Input
# -----------------------------
st.subheader("🔎 Analyze a Message")

message = st.text_area(
    "Paste the suspicious message below:",
    height=180,
    placeholder="Example: Congratulations! You have been selected for..."
)

analyze = st.button(
    "🔍 Analyze Message",
    type="primary",
    use_container_width=True
)

# -----------------------------
# Analysis Function
# -----------------------------
def analyze_message(text):
    text = text.lower()

    warning_patterns = {
        "Urgent language": [
            "urgent",
            "immediately",
            "act now",
            "within 24 hours",
            "last chance"
        ],
        "Payment request": [
            "pay",
            "payment",
            "fee",
            "registration fee",
            "processing fee",
            "deposit"
        ],
        "Credential request": [
            "password",
            "otp",
            "one time password",
            "pin",
            "cvv"
        ],
        "Suspicious link/action": [
            "click this link",
            "click here",
            "verify your account",
            "open this link"
        ],
        "Prize or reward claim": [
            "you have won",
            "winner",
            "congratulations",
            "selected",
            "claim your reward",
            "free reward"
        ]
    }

    findings = []

    for category, keywords in warning_patterns.items():
        matched = []

        for keyword in keywords:
            if keyword in text:
                matched.append(keyword)

        if matched:
            findings.append((category, matched))

    return findings


# -----------------------------
# Results
# -----------------------------
if analyze:

    if not message.strip():
        st.warning("Please paste a message first.")

    else:
        findings = analyze_message(message)

        st.divider()
        st.subheader("📊 Analysis Result")

        if findings:

            st.warning(
                f"ScamShield identified **{len(findings)} potential warning area(s)**."
            )

            st.markdown(
                '<div class="result-card"><h3>⚠️ Potential Warning Signs</h3>',
                unsafe_allow_html=True
            )

            for category, keywords in findings:

                words = ", ".join(f"`{word}`" for word in keywords)

                st.markdown(
                    f"""
                    <div class="warning-item">
                        <strong>{category}</strong><br>
                        Detected indicators: {words}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            st.markdown("</div>", unsafe_allow_html=True)

            # -----------------------------
            # Why concerning
            # -----------------------------
            st.markdown(
                '<div class="result-card"><h3>💡 Why These May Be Concerning</h3>',
                unsafe_allow_html=True
            )

            explanations = {
                "Urgent language":
                    "Pressure to act immediately can discourage users from taking time to verify a request.",

                "Payment request":
                    "Unexpected fees or requests for money should be independently verified before making any payment.",

                "Credential request":
                    "Sensitive information such as OTPs, passwords, PINs, or CVVs should not normally be shared with unknown people or services.",

                "Suspicious link/action":
                    "Links asking you to verify or claim something should be checked carefully and preferably accessed through an official website.",

                "Prize or reward claim":
                    "Unexpected prizes or rewards can be used to persuade users to click links, provide information, or make payments."
            }

            for category, _ in findings:
                st.markdown(
                    f"""
                    <div class="warning-item">
                        <strong>{category}</strong><br>
                        {explanations[category]}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            st.markdown("</div>", unsafe_allow_html=True)

            # -----------------------------
            # Safer actions
            # -----------------------------
            st.markdown(
                '<div class="result-card"><h3>🛡️ Safer Next Steps</h3>',
                unsafe_allow_html=True
            )

            safer_steps = [
                "Do not send money until the request has been independently verified.",
                "Do not share OTPs, passwords, PINs, CVVs, or other sensitive information.",
                "Avoid clicking suspicious links.",
                "Verify the organization using its official website or contact details.",
                "If the message claims to be from a company, contact that company through an independently verified channel."
            ]

            for step in safer_steps:
                st.markdown(
                    f'<div class="safe-item">✓ {step}</div>',
                    unsafe_allow_html=True
                )

            st.markdown("</div>", unsafe_allow_html=True)

        else:

            st.success(
                "No common warning patterns were detected in this message."
            )

            st.info(
                "This does not guarantee that the message is safe. "
                "Always verify unexpected requests through trusted official sources."
            )

# -----------------------------
# Disclaimer
# -----------------------------
st.divider()

st.markdown("""
<div class="disclaimer">
<strong>Important:</strong> ScamShield AI provides informational guidance.
It does not guarantee that a message is legitimate or fraudulent.
Always independently verify important requests through trusted official sources.
</div>
""", unsafe_allow_html=True)