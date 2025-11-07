# 🌐 Deploying a Reflex App to Render with a Custom Squarespace Domain

This guide documents the **exact working process** used to deploy the `my_portfolio_site` Reflex app (built with Python) to Render — with a working custom domain `https://www.biodataworks.com` registered through Squarespace.

It’s written for anyone deploying a **Reflex app** (formerly Pynecone) with both frontend and backend bundled together, using Reflex’s own `reflex run` command instead of Uvicorn or a manual backend setup.

---

## 🧠 What This App Does

Reflex automatically creates a full-stack Python web app:
- **Frontend** (the visual website, served by Reflex)
- **Backend** (the API + WebSocket layer that powers interactivity)

You don’t need to separate them — Reflex handles it all internally.

---

## 🏗️ 1. Folder Structure

Your working folder layout looks like this:

        my-portfolio-site/
        ├── assets/
        │ ├── biodataworks_logo.png
        │ ├── me.jpg
        │ └── resume.pdf
        ├── frontend/
        │ ├── index.html
        │ └── assets/
        ├── my_portfolio_site/
        │ ├── init.py
        │ └── my_portfolio_site.py
        ├── rxconfig.py
        ├── requirements.txt
        └── ...


Key points:
- You **don’t** need a separate `backend/` directory.
- The `frontend/` folder comes from unzipping your exported `frontend.zip`.
- Reflex serves both layers together automatically.

---

## ⚙️ 2. `rxconfig.py` Configuration

Here’s the working configuration that allows both Render and your custom Squarespace domain to connect:

```python
import reflex as rx

config = rx.Config(
    app_name="my_portfolio_site",
    allowed_hosts=[
        "my-portfolio-site-s173.onrender.com",
        "localhost",
        "www.biodataworks.com",
        "biodataworks.com",
    ],
    cors_allowed_origins=[
        "https://my-portfolio-site-s173.onrender.com",
        "http://localhost:3000",
        "https://www.biodataworks.com",
        "https://biodataworks.com",
    ],
    disable_plugins=['reflex.plugins.sitemap.SitemapPlugin'],
)
```

This ensures:

  * Your Render app and your Squarespace domain can make cross-origin requests (CORS).

  * WebSocket connections work correctly across HTTPS (wss://).


## 💻 3. Local Testing

To verify everything works locally:

```bash
reflex run
```

Then open: [http://localhost:3000](http://localhost:3000)

You should see your app running correctly.
If you do, you’re ready to deploy!


## ☁️ 4. Deploying to Render

### Step 1: Connect to Render

  1. Go to https://render.com

  2. Create a new Web Service

  3. Connect your GitHub repo

  4. Choose your app’s root directory (the same folder containing rxconfig.py)

  5. Environment: Python 3

### Step 2: Set the Build and Start Commands

In Render’s dashboard (Project > Settings):

  * Build Command:

        pip install -r requirements.txt

  * Start Command:

        reflex run --env prod --backend-host 0.0.0.0 --backend-port 10000 --frontend-port 10000

Note: I still get the warning about specifying ports every time. *No open ports detected, continuing to scan...* but at least this directs both ports to the same place and on the preferred port of 10000. You should hypothetically be able to use `$PORT` instead of `10000`, which is best practice since that environmental variable is set by Render. 


### Step 3: Confirm Successful Deployment

Render logs should show: `==> Your service is live 🎉`

Your app is now live at your Render domain, e.g.: [https://my-portfolio-site-s173.onrender.com](https://my-portfolio-site-s173.onrender.com)


## 🌍 5. Connecting a Squarespace Domain

You can make your Squarespace domain point to your Render app.

### Step 1: Add Custom Domains in Render

In your Render service → Settings → Custom Domains, add both: www.biodataworks.com and biodataworks.com. 

Render will show DNS records to add in Squarespace (usually a CNAME and an A record).

### Step 2: Update DNS Records in Squarespace

In Squarespace → Domains → DNS Settings:

Delete the Squarespace defaults (trashcan icon). It includes a CNAME for www that will conflict with your Render CNAME.

Add Render’s CNAME for www exactly as shown in your Render DNS records on your render project page. For example, mine were as follows. 

  * host = wwww
  * type = CNAME
  * data = my-portfolio-site-s173.onrender.com

as well as

  * host = @
  * type = ALIAS
  * data = my-portfolio-site-s173.onrender.com

Save your changes.

Wait 10–30 minutes for DNS to propagate.

When it's ready, you'll see "Certificate Issued" in your Render app Settings under the Custom Domains section next to each listed domain. 

