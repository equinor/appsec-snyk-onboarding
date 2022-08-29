# Generate QR link to site

```
cd scripts/
python -m venv env
source env/bin/activate
pip install -r requirements.txt
qr 'https://snykonboarding.app.radix.equinor.com/' > ../content/images/snykonboarding_qr.png
```
