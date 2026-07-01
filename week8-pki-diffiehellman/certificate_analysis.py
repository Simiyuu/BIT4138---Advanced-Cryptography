def certificate_report(website, issuer, subject, issued_on, expiry, fingerprint):
    print("=== Certificate Analysis Report ===\n")
    print(f"Website Analyzed:     {website}")
    print(f"Subject (CN):         {subject}")
    print(f"Issuing CA:           {issuer}")
    print(f"Issued On:            {issued_on}")
    print(f"Expiry Date:          {expiry}")
    print(f"Certificate Fingerprint: {fingerprint}")
    print("\n=== Observations ===")
    print("The certificate confirms the website's identity was verified")
    print("by a trusted Certificate Authority (Amazon) before being issued.")
    print("This allows the browser to establish a secure TLS connection")
    print("and protects users from man-in-the-middle attacks.")
    print("The validity period ensures the certificate is regularly")
    print("renewed, reducing the risk of using outdated or compromised keys.")

certificate_report(
    website="www.netacad.com",
    issuer="Amazon RSA 2048 M01 (Amazon)",
    subject="www.netacad.com",
    issued_on="Wednesday, June 24, 2026 at 3:00:00 AM",
    expiry="Friday, January 8, 2027 at 2:59:59 AM",
    fingerprint="f8b78c1fc55e8314144541e38866fc4bb18da70f7cd88a4e8b656b9e87b8bee3"
)