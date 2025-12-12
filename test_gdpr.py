from app import init_database, display_users, anonymize_data, truncate_personal_fields

def test_anonymization():
    print("Running GDPR anonymization test...\n")
    init_database()
    display_users()
    print("\nAnonymizing data...\n")
    anonymize_data()
    display_users()
    print("\nTruncating data...\n")
    truncate_personal_fields()
    display_users()
    print("\nTest completed successfully.")

if __name__ == "__main__":
    test_anonymization()



