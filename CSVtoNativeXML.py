import csv
import xml.etree.ElementTree as ET

# Initialize the XML structure
root = ET.Element("Native", xmlns="http://www.cargowise.com/Schemas/Native/2011/11", version="2.0")
header = ET.SubElement(root, "Header")
ET.SubElement(header, "OwnerCode").text = "INTCARLON"
ET.SubElement(header, "EnableCodeMapping").text = "true"
body = ET.SubElement(root, "Body")

# Read the CSV file
with open('contactList.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        organization = ET.SubElement(body, "Organization", version="2.0")
        org_header = ET.SubElement(organization, "OrgHeader", Action="UPDATE")
        
        ET.SubElement(org_header, "Code").text = row["Organisation Code"]
        ET.SubElement(org_header, "FullName").text = row["Full Name"]

        org_contact_collection = ET.SubElement(org_header, "OrgContactCollection")
        org_contact = ET.SubElement(org_contact_collection, "OrgContact", Action="MERGE")
        
        ET.SubElement(org_contact, "ContactName").text = row["Contact Name"]
        ET.SubElement(org_contact, "Language").text = "EN"
        ET.SubElement(org_contact, "NotifyMode").text = "EML"
        ET.SubElement(org_contact, "Title").text = row["Job Title"] or ""
        ET.SubElement(org_contact, "JobCategory").text = "ONS"
        ET.SubElement(org_contact, "Phone").text = ""
        ET.SubElement(org_contact, "PhoneExtension").text = ""
        ET.SubElement(org_contact, "Fax").text = ""
        ET.SubElement(org_contact, "HomePhone").text = row["Phone Work"].split(',')[0].strip() if row["Phone Work"] else ""
        ET.SubElement(org_contact, "Mobile").text = row["Phone Mobile"].split(',')[0].strip() if row["Phone Mobile"] else ""
        ET.SubElement(org_contact, "AttachmentType").text = "PDF"
        ET.SubElement(org_contact, "IsActive").text = "true"
        ET.SubElement(org_contact, "Email").text = row["Email"]
        ET.SubElement(org_contact, "Code").text = ""

# Convert to string and save the XML
xml_str = ET.tostring(root, encoding='utf-8', xml_declaration=True)
with open('output.xml', 'wb') as output_file:
    output_file.write(xml_str)

print("XML conversion complete. Check output.xml.")
