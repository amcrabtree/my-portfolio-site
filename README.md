# Portfolio Website

Modified from Dr. Aditya Kumar Gupta's repo: https://github.com/aditya30051993/my-portfolio/

Live at: [https://amcrabtree.github.io/my-portfolio-site](https://amcrabtree.github.io/my-portfolio-site)

## Setup for Development

To set up the project for development, follow these steps:

1. Clone the repository & navigate to the project directory:

   ```
   git clone https://github.com/aditya30051993/my-portfolio.git; cd my-portfolio
   ```

2. Install dependencies & Start the development server:

   ```
   npm install; npm start
   ```

The project will be running at `http://localhost:3000` and will automatically reload when you make changes.

## Updating Your Data

Ensure the JSON files in `src/data` are updated with your information. After updating them, in `src` run the following command:

```
node generate-resume.js
```

This will generate `resume.pdf` in the `public` folder.

## Deploying to GitHub Pages

To deploy your project to GitHub Pages, follow these steps:

1. Add the following properties to your `package.json`:

   ```json
   "homepage": "https://amcrabtree.github.io/my-portfolio-site",
   ```

2. Deploy the project:
   ```
   npm run deploy
   ```

Your project will be available at `https://amcrabtree.github.io/my-portfolio-site`.
