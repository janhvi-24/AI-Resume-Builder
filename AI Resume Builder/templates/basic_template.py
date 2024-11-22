def basic_template(pdf, name, contact, education, experience, skills, additional):
    pdf.add_section("Name", name)
    pdf.add_section("Contact Information", contact)
    pdf.add_section("Education", education)
    pdf.add_section("Experience", experience)
    pdf.add_section("Skills", skills)
    if additional:
        pdf.add_section("Additional Information", additional)
