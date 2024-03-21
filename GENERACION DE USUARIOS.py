def generate_email(name, last_name, birthdate, domain="gmail"):
    # Obtener las primeras dos letras del nombre y las últimas dos del apellido
    user = name[:2].lower() + last_name[-2:].lower()

    # Obtener el día de nacimiento
    day = birthdate.split("/")[0]

    # Generar el correo electrónico
    email = user + day + "@" + domain + ".com"

    return email

# Ejemplo de uso
name = "Erick"
last_name = "Borges"
birthdate = "5/10/99"
domain = "hotmail"

email = generate_email(name, last_name, birthdate, domain)
print(email)  # eres05@hotmail.com