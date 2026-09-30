# ScamShield AI – Student Digital Safety Assistant

ScamShield AI is a student-focused digital safety assistant that helps users understand suspicious messages before they click links, share information, or make payments.

The application analyzes a message for common warning signs and explains them in simple language, followed by practical safety steps.

## 🎯 Problem

Students regularly receive suspicious:

* Job and internship offers
* Scholarship messages
* Payment requests
* Prize and reward messages
* Account verification messages
* SMS, WhatsApp, and email messages

Many students may not know which warning signs to look for or what they should do next.

## 💡 Solution

ScamShield AI allows a user to paste a suspicious message into the application.

The application identifies potential warning signs such as:

* Urgent or pressure-based language
* Payment or fee requests
* Requests for passwords, OTPs, PINs, or CVVs
* Suspicious links or verification requests
* Prize or reward claims

It then explains why these signals may be concerning and provides safer next steps.

The goal is **not to make the decision for the user**, but to help them understand potential risks before taking action.

## ✨ Key Features

* 🔎 Suspicious message analysis
* ⚠️ Potential warning-sign detection
* 📖 Simple explanations of detected signals
* 🛡️ Practical safety recommendations
* 🎓 Student-focused digital safety guidance
* 🔐 Privacy-conscious design
* 📱 Simple and beginner-friendly interface

## 🧠 Current Analysis

The current MVP uses rule-based detection to identify common warning signs in suspicious messages.

Example warning areas include:

| Warning Area       | Examples                                 |
| ------------------ | ---------------------------------------- |
| Urgent Language    | `immediately`, `act now`, `last chance`  |
| Payment Request    | `fee`, `payment`, `deposit`              |
| Credential Request | `OTP`, `password`, `PIN`, `CVV`          |
| Suspicious Action  | `click this link`, `verify your account` |
| Prize / Reward     | `you have won`, `claim your reward`      |

## 🛡️ Safer Next Steps

When potential warning signs are detected, ScamShield AI recommends users to:

1. Avoid sending money until the request is independently verified.
2. Never share OTPs, passwords, PINs, or CVVs.
3. Avoid clicking suspicious links.
4. Verify the organization using its official website or trusted contact information.
5. Contact the organization through an independently verified communication channel.

## ☁️ AWS Development

ScamShield AI is being developed for the **AWS Zero to Shipped Hackathon 2026**.

The current project includes AWS deployment preparation using:

* Amazon ECR for container image storage
* AWS CodeBuild for container build automation
* Amazon ECS Express Mode as the planned application hosting platform

The AWS deployment is currently in progress.

Future development may include AI-powered analysis using Amazon Bedrock and additional AWS services where they provide clear value to the application.

## 🏗️ Project Structure

```text
ScamShield-AI/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── Procfile
├── buildspec.yml
├── .gitignore
└── README.md
```

## 🚀 Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/shreyabpatel632008-sudo/ScamShield-AI.git
cd ScamShield-AI
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the application

```bash
python -m streamlit run app.py
```

The application will open in your browser.

## 🔒 Important Note

ScamShield AI provides **informational guidance only**.

A detected warning sign does not automatically mean that a message is fraudulent, and the absence of warning signs does not guarantee that a message is legitimate.

Users should independently verify important requests through trusted official sources before taking action.

## 🌱 Community Impact

ScamShield AI is designed with students and young digital users in mind.

The project focuses on improving digital safety awareness by explaining **why** a message may deserve caution instead of simply providing a yes/no answer.

The aim is to help users develop better habits when dealing with unfamiliar digital communication.

## 📌 Project Status

**Status:** MVP completed — AWS deployment in progress

**Category:** Social Good – Education

**Lane:** Community

**Hackathon:** AWS Zero to Shipped Hackathon 2026

## 👩‍💻 Developer

**Shreya Patel**

Computer Engineering Student
Government Engineering College, Palanpur

## 📂 Repository

GitHub: https://github.com/shreyabpatel632008-sudo/ScamShield-AI
