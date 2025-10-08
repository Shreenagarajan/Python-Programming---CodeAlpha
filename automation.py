import re
import os

def extract_emails(input_file, output_file):
    """
    Extract all email addresses from a text file and save them to another file.
    """
    try:
        # Check if input file exists
        if not os.path.exists(input_file):
            print("❌ Input file not found. Please check the file path.")
            return
        
        # Read content from input file
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Use regex to find all email addresses
        emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
        
        # Remove duplicates (optional)
        unique_emails = sorted(set(emails))
        
        # Save results to output file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write("Extracted Email Addresses:\n")
            file.write("-" * 40 + "\n")
            for email in unique_emails:
                file.write(email + "\n")
        
        # Display result
        print(f"\n✅ Extracted {len(unique_emails)} unique email(s).")
        print(f"📄 Saved results to: {output_file}")
    
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")


# ------------------- MAIN PROGRAM -------------------

print("📧 Email Extractor Automation")
print("This script extracts all email addresses from a text file.\n")

# Ask user for file names
input_path = input("Enter the path of your input text file (e.g., sample_text.txt): ").strip()
if input_path == "":
    input_path = "sample_text.txt"  # default fallback

output_path = input("Enter a name for the output file (default: extracted_emails.txt): ").strip()
if output_path == "":
    output_path = "extracted_emails.txt"

# Run the extraction
extract_emails(input_path, output_path)

print("\n✅ Task Completed Successfully!")
print("💡 Tip: Open the output file to see the extracted emails.")



