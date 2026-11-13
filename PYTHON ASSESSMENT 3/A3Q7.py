
import re

# Contacts from different devices
contacts = [
    {
        "name": "Dr. Ravi",
        "phone": "+91 98400 12345",
        "email": "ravi@gmail.com"
    },
    {
        "name": "Ravi Kumar",
        "phone": "9840012345",
        "email": "ravi@gmail.com"
    },
    {
        "name": "Arun",
        "phone": "+91 98765 43210",
        "email": "arun@gmail.com"
    },
    {
        "name": "Priya",
        "phone": "9876543211",
        "email": "priya@gmail.com"
    },
    {
        "name": "Arun",
        "phone": "9876543210",
        "email": "arun@yahoo.com"
    }
]

# Normalize phone numbers
def normalize_phone(phone):
    if not phone:
        return ""

    digits = re.sub(r"\D", "", phone)

    if digits.startswith("91") and len(digits) == 12:
        digits = digits[2:]

    return digits

# Merge contacts
merged = {}

for contact in contacts:
    phone = normalize_phone(contact.get("phone", ""))
    email = contact.get("email", "").strip().lower()
    name = contact.get("name", "").strip()

    # Use phone as primary key and email as fallback
    key = phone if phone else (
        "email:" + email if email else "unique:" + str(id(contact))
    )

    if key not in merged:
        merged[key] = {
            "names": set(),
            "phones": set(),
            "emails": set()
        }

    if name:
        merged[key]["names"].add(name)

    if phone:
        merged[key]["phones"].add(phone)

    if email:
        merged[key]["emails"].add(email)

# Display merged contacts
print("Merged Contacts")

for key, details in merged.items():
    print("\nNames:", sorted(details["names"]))
    print("Phone Numbers:", sorted(details["phones"]))
    print("Email Addresses:", sorted(details["emails"]))
