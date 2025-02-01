import re
from datetime import datetime

# Keywords and patterns for detection
GOVERNMENT_KEYWORDS = [
    "aadhaar", "pan card", "income tax", "gst", "epf", "pm kisan",
    "pmjay", "uidai", "itr", "seva kendra", "kyc", "upi", "bank",
    "neft", "rtgs", "voter id", "pf withdrawal", "tax refund"
]

SCAM_PATTERNS = [
    r"\b(verify|update|reactivate)\b.*\b(aadhaar|pan|kyc)\b",
    r"\b(won|winner|prize|reward)\b.*\b(gov|government|india)\b",
    r"\b(urgent|immediate)\b.*\b(action|response)\b",
    r"\b(otp|password|pin)\b.*\b(share|provide|enter)\b",
    r"\b\d{4}[\s-]?\d{4}[\s-]?\d{4}\b",  # Aadhaar-like numbers
    r"\b[A-Z]{5}\d{4}[A-Z]{1}\b"  # PAN-like pattern
]

def get_safety_recommendations(message_type):
    """Return safety recommendations based on message type."""
    recommendations = {
        "financial": [
            "1. DO NOT share any OTP or password",
            "2. Report to your bank immediately",
            "3. Check your bank account for unauthorized transactions",
            "4. File a complaint on cybercrime.gov.in",
            "5. Block the sender's number",
            "6. Take screenshots as evidence"
        ],
        "identity": [
            "1. DO NOT click on any links",
            "2. Report to respective authority (UIDAI for Aadhaar, IT dept for PAN)",
            "3. File a police complaint",
            "4. Document all communication",
            "5. Monitor your credit report",
            "6. Report on cybercrime.gov.in"
        ],
        "general": [
            "1. Block the sender immediately",
            "2. Report the number to your telecom provider",
            "3. File a complaint on cybercrime.gov.in",
            "4. Save the message as evidence",
            "5. Alert friends and family about this scam"
        ]
    }
    return recommendations.get(message_type, recommendations["general"])

def analyze_message_type(message):
    """Determine the type of potential scam."""
    message = message.lower()
    if any(word in message for word in ["bank", "upi", "account", "money", "payment"]):
        return "financial"
    elif any(word in message for word in ["aadhaar", "pan", "voter", "identity"]):
        return "identity"
    return "general"

def is_fake_sms(message):
    """Check if message is fake and return analysis."""
    msg_lower = message.lower()
    matched_patterns = []
    
    # Check government keywords
    for keyword in GOVERNMENT_KEYWORDS:
        if keyword in msg_lower:
            matched_patterns.append(f"Contains sensitive keyword: {keyword}")
    
    # Check scam patterns
    for pattern in SCAM_PATTERNS:
        if re.search(pattern, msg_lower):
            matched_patterns.append(f"Matches suspicious pattern: {pattern}")
    
    return bool(matched_patterns), matched_patterns

def main():
    print("\n=== Fake SMS Detection System ===")
    print("This system will help you identify potential scam messages and guide you on next steps.")
    
    while True:
        print("\n" + "="*50)
        message = input("\nEnter the message to check (or 'exit' to quit): ")
        
        if message.lower() == 'exit':
            print("\nThank you for using the Fake SMS Detection System. Stay safe!")
            break
        
        is_fake, patterns = is_fake_sms(message)
        
        print("\nAnalysis Result:")
        print("-" * 20)
        
        if is_fake:
            print("⚠️ WARNING: This message appears to be FAKE!")
            print("\nReason(s) for detection:")
            for pattern in patterns:
                print(f"- {pattern}")
            
            message_type = analyze_message_type(message)
            print(f"\nRecommended actions for {message_type} scam:")
            print("-" * 40)
            
            recommendations = get_safety_recommendations(message_type)
            for rec in recommendations:
                print(rec)
                
            print("\nImportant Contact Information:")
            print("- Cyber Crime Portal: cybercrime.gov.in")
            print("- Emergency Cyber Crime Helpline: 1930")
            print("- Police Emergency: 112")
        else:
            print("✅ This message appears to be legitimate.")
            print("\nHowever, always exercise caution and:")
            print("- Never share sensitive information via SMS")
            print("- Be wary of unexpected requests")
            print("- When in doubt, verify through official channels")
        
        print("\nWould you like to check another message?")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user. Stay safe!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please try again.")