def explain_pki_components():
    components = {
        "Certificate Authority (CA)": "A trusted organization that verifies identities, issues digital certificates, and revokes them when necessary. Maintains overall trust in the PKI system.",
        "Registration Authority (RA)": "Acts as an intermediary between users and the CA. Verifies user identity and approves certificate requests before forwarding them to the CA.",
        "Digital Certificate": "An electronic document that binds a public key to an individual or organization, containing details like the owner, issuing CA, validity period, and digital signature.",
        "End User": "Individuals, systems, or organizations that use certificates, such as website owners, email users, banks, or government agencies.",
        "Certificate Repository": "A database where issued certificates are stored and can be accessed or verified by other parties."
    }

    print("=== PKI Component Identification ===\n")
    for component, role in components.items():
        print(f"{component}:")
        print(f"  {role}\n")

explain_pki_components()