# Onuralp Sezer - Portfolio

A modern portfolio website built with [Astro](https://astro.build).

## Tech Stack

- **Framework:** Astro 5
- **Styling:** CSS with custom properties
- **Fonts:** Inter, JetBrains Mono
- **Package Manager:** Bun

## Development

```bash
# Install dependencies
bun install

# Start development server
bun run dev

# Build for production
bun run build

# Preview production build
bun run preview
```

## Deployment

This site is deployed to GitHub Pages using GitHub Actions. The workflow automatically builds and deploys on pushes to the `portfolio-site` branch.

## Project Structure

```
├── src/
│   ├── components/     # Reusable UI components
│   ├── content/        # Markdown content for projects
│   ├── layouts/        # Page layouts
│   ├── pages/          # Route pages
│   └── styles/         # Global styles
├── public/             # Static assets
└── .github/workflows/  # GitHub Actions
```

## License

MIT
