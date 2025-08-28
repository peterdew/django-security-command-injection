# Django Command Injection Vulnerability Demo

Een Django oefening die demonstreert hoe command injection vulnerabilities kunnen ontstaan door onveilige subprocess calls.

## 🎯 Doel

Deze oefening toont een command injection vulnerability in een Django management commando. Het doel is om te leren hoe gevaarlijk het is om user input direct in shell commando's te gebruiken.

## ⚠️ Waarschuwing

**Dit is een opzettelijk kwetsbare applicatie voor educatieve doeleinden. Gebruik dit NOOIT in productie!**

## 🐧 Vereisten

- Linux besturingssysteem
- Python 3.7+
- Django 3.0+
- MySQL (voor mysqldump commando)

## 🚀 Installatie

```bash
# Clone de repository
git clone https://github.com/peterdew/django-security-command-injection.git
cd django-security-command-injection

# Ga naar de Django project directory
cd vulndemo

# Installeer dependencies (als je een requirements.txt hebt)
pip install django

# Run migrations (als je een database hebt)
python manage.py migrate
```

## 🧪 De Vulnerability

De vulnerability zit in `vulndemo/vulndemo/management/commands/backup_user.py`:

```python
# KWETSBAAR: Direct user input in shell command
cmd = f"mysqldump -u root mydb_users_{username} > backup_{username}.sql"
subprocess.call(cmd, shell=True)
```

Het probleem is dat de `username` parameter direct in een shell commando wordt geplaatst zonder validatie.

## 🎮 Gebruik

### Legitiem gebruik:
```bash
python manage.py backup_user --username john_doe
```

### Command Injection voorbeelden:
```bash
# Directory listing
python manage.py backup_user --username "test; ls -la"

# System info
python manage.py backup_user --username "test; uname -a"

# Create a file
python manage.py backup_user --username "test; echo 'Hacked!' > hacked.txt"

# Show current user
python manage.py backup_user --username "test; whoami"

# Network info
python manage.py backup_user --username "test; ifconfig"
```

## 🔍 Hoe het werkt

1. Het Django management commando neemt een `--username` parameter
2. Deze wordt direct in een `mysqldump` commando geplaatst
3. Door de username te manipuleren met shell operators (`;`, `&&`, `|`), kunnen willekeurige commando's worden uitgevoerd
4. Het `shell=True` argument maakt dit mogelijk

## 🛡️ Veilige Oplossing

Om deze vulnerability te voorkomen:

```python
# ❌ ONVEILIG
cmd = f"mysqldump -u root mydb_users_{username} > backup_{username}.sql"
subprocess.call(cmd, shell=True)

# ✅ VEILIG
import shlex
args = ["mysqldump", "-u", "root", f"mydb_users_{username}"]
with open(f"backup_{username}.sql", "w") as f:
    subprocess.run(args, stdout=f, shell=False)
```

## 📚 Leerdoelen

- Begrijpen hoe command injection werkt
- Herkennen van onveilige subprocess calls
- Leren over input validation
- Begrijpen van shell operators
- Best practices voor veilige command execution

## 🔧 Troubleshooting

### mysqldump niet gevonden
```bash
# Installeer MySQL client
sudo apt-get install mysql-client

# Of voor Ubuntu/Debian
sudo apt-get install default-mysql-client
```

### Permissie problemen
```bash
# Zorg ervoor dat je schrijfrechten hebt in de huidige directory
chmod 755 .
```

## 📝 Notities

- Deze demo werkt alleen in Linux omdat `mysqldump` een Linux/Unix commando is
- Voor Windows zou je een equivalent commando moeten gebruiken
- De vulnerability is opzettelijk eenvoudig gehouden voor educatieve doeleinden

## 🤝 Bijdragen

Pull requests zijn welkom! Voor grote wijzigingen, open eerst een issue om te bespreken wat je wilt veranderen.

## 📄 Licentie

Dit project is voor educatieve doeleinden. Gebruik op eigen risico. 