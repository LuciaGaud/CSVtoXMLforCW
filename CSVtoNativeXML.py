import csv
import xml.etree.ElementTree as ET

# Prompt for the three-digit company code
company_code = input("Enter the three-digit company code. Example SWL: ")

# Initialize the XML structure
root = ET.Element("Native", xmlns="http://www.cargowise.com/Schemas/Native/2011/11", version="2.0")
header = ET.SubElement(root, "Header")
ET.SubElement(header, "OwnerCode").text = "INTCARLON"
ET.SubElement(header, "EnableCodeMapping").text = "true"
body = ET.SubElement(root, "Body")

# Read the CSV file
with open('contactList.csv', mode='r', newline='', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    print("CSV Headers:", reader.fieldnames)
    
    for row in reader:
        # Create Organization section
        organization = ET.SubElement(body, "Organization", version="2.0")
        org_header = ET.SubElement(organization, "OrgHeader", Action="UPDATE")
        org_companyDataCollection = ET.SubElement(org_header, "OrgCompanyDataCollection")
        org_companyData = ET.SubElement(org_companyDataCollection, "OrgCompanyData", Action="UPDATE")
        
        # Fill in Organization details
        ET.SubElement(org_header, "Code").text = row["Organisation Code"]
        ET.SubElement(org_header, "JobCategory").text = row["Job Category"]

        # Create Organization Company Data section
        controllingBranch = ET.SubElement(org_companyData, "ControllingBranch", Action="UPDATE")
        ET.SubElement(controllingBranch, "Code").text = row["Controlling Branch"]
        GlbCompany = ET.SubElement(org_companyData, "GlbCompany")
        ET.SubElement(GlbCompany, "Code").text = company_code

        # Create OrgContactCollection
        org_contact_collection = ET.SubElement(org_header, "OrgContactCollection")
        org_contact = ET.SubElement(org_contact_collection, "OrgContact", Action="MERGE")
        
        # Fill in OrgContact details
        ET.SubElement(org_contact, "ContactName").text = row["Contact Name"]
        ET.SubElement(org_contact, "Language").text = "EN"
        ET.SubElement(org_contact, "NotifyMode").text = "EML"
        ET.SubElement(org_contact, "Title").text = row["Job Title"][:35] or ""
        ET.SubElement(org_contact, "JobCategory").text = row["Job Category"]

        # Format phone numbers and add fields
        ET.SubElement(org_contact, "Phone").text = row["PhoneWork"].split(',')[0].strip().replace("'", "")
        ET.SubElement(org_contact, "PhoneExtension").text = ""
        ET.SubElement(org_contact, "Fax").text = ""
        ET.SubElement(org_contact, "HomePhone").text = ""
        ET.SubElement(org_contact, "Mobile").text = row["PhoneMobile"].split(',')[0].strip().replace("'", "")
        ET.SubElement(org_contact, "AttachmentType").text = "PDF"
        ET.SubElement(org_contact, "IsActive").text = "true"
        ET.SubElement(org_contact, "Email").text = row["Email"]
        ET.SubElement(org_contact, "Code").text = ""

# Convert to string and save the XML
xml_str = ET.tostring(root, encoding='utf-8', xml_declaration=True)
with open('output.xml', 'wb') as output_file:
    output_file.write(xml_str)

print("XML conversion complete. Check output.xml.")
