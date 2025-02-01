# Fake SMS Detection System 🛡️

A Python-based tool to detect potential scam SMS messages, particularly those impersonating government services and financial institutions in India. The system analyzes messages for suspicious patterns and provides safety recommendations based on the type of potential scam.

## 🎯 Features

- Real-time SMS scam detection
- Pattern-based analysis for common scam types
- Detection of sensitive government keywords
- Recognition of financial and identity theft attempts
- Customized safety recommendations based on scam type
- Emergency contact information
- User-friendly command-line interface

## 🔍 Scam Types Detected

- Financial scams (UPI, bank-related)
- Identity theft (Aadhaar, PAN card)
- Government impersonation
- Prize and lottery scams
- KYC fraud attempts
- OTP theft attempts

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/fake-sms-detection.git
cd fake-sms-detection
```

2. No additional dependencies required - runs with Python standard library.

## 💻 Usage

Run the script:
```bash
python fake_sms_detection.py
```

Follow the interactive prompts:
1. Enter the SMS message you want to check
2. Review the analysis results
3. Follow safety recommendations if a scam is detected
4. Type 'exit' to quit the program

## 📌 Example

```python
=== Fake SMS Detection System ===
This system will help you identify potential scam messages and guide you on next steps.

Enter the message to check (or 'exit' to quit): 
URGENT: Your Aadhaar card will be deactivated today. Share OTP 4523 to reactivate: +91XXXXXXXXXX

Analysis Result:
--------------------
⚠️ WARNING: This message appears to be FAKE!

Reason(s) for detection:
- Contains sensitive keyword: aadhaar
- Matches suspicious pattern: \b(urgent|immediate)\b.*\b(action|response)\b
- Matches suspicious pattern: \b(otp|password|pin)\b.*\b(share|provide|enter)\b
```

## 🔒 Security Features

- Detection of Aadhaar number patterns
- PAN card number pattern recognition
- Identification of suspicious URLs
- Recognition of urgent/threatening language
- Detection of requests for sensitive information

## 🚀 Future Enhancements

- Machine learning-based detection
- SMS forwarding integration
- Mobile app interface
- Database of known scam patterns
- Automated reporting to authorities
- Multi-language support

## ⚠️ Disclaimer

This tool is meant to assist in identifying potential scams but should not be considered foolproof. Always exercise caution with unexpected messages and verify through official channels when in doubt.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Important Contacts

- Cyber Crime Portal: cybercrime.gov.in
- Emergency Cyber Crime Helpline: 1930
- Police Emergency: 112

## 👥 Authors

- Your Name - *Initial work*

## 🙏 Acknowledgments

- Indian Cyber Crime Coordination Centre
- Ministry of Home Affairs, Government of India
- Cyber Security Community

---
⚡️ Remember: Never share OTP, passwords, or sensitive information via SMS!
