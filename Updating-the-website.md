# Updating the Excelsior Fencing Club website

This guide explains how the public site is built, where content lives, and how to publish changes using GitHub.

**Live site:** https://www.excelsiorfencing.ca  
**Website repository:** https://github.com/Excelsior-Fencing-Club/Excelsior-fencing-website  
**Publishing:** GitHub Pages builds from the `main` branch automatically after each merge.

This file lives in the repo root for easy editing on GitHub. It is listed under `exclude` in `_config.yml` so Jekyll does not build it — the examples below contain `{% include_relative %}` tags that would otherwise break the site build.

---

## What this site is (and is not)

The website repo contains **public-facing content only**: news, schedules, coach bios, program information, and club photos.

Internal club operations (board minutes, invoices, vulnerable sector checks, grants, bylaws) belong in the separate **Excelsior-Fencing-Club** repository, not on the public site.

| Topic | Edit in website repo | Edit in club ops repo |
|-------|----------------------|------------------------|
| News, calendar, coaches (public) | Yes | No |
| Board minutes, VSC, invoices | No | Yes |
| WellnessLiving membership backend | No | Yes (org docs) |

---

## How the site works

- **Jekyll** turns Markdown (`.md`) files into HTML pages.
- **GitHub Pages** hosts the built site at `excelsiorfencing.ca` (see `CNAME` in the repo root).
- **Theme:** [GitHub Pages “hacker” theme](https://github.com/pages-themes/hacker) via `_config.yml` (`remote_theme: pages-themes/hacker@v0.2.0`).
- **Custom layout:** `_layouts/default.html` adds the site banner, navigation table, and styling around each page’s content.
- **Obsidian:** The repo is also an Obsidian vault (`.obsidian/`). Many editors use Obsidian locally for preview and note-taking; publishing still happens through GitHub.

Most pages start with YAML **frontmatter** (metadata between `---` lines):

```yaml
---
image:
  path: /images/Excelsior-logo.png
  type: image/png
  alt: Excelsior Fencing Club
description: "Short summary for search engines"
site_name: Excelsior Fencing Club
title: "Page title shown in the browser tab"
---
```

Body content below the frontmatter is normal Markdown (headings, lists, links). Some pages (notably `Coaches.md`) also use HTML tables for layout.

---

## Site navigation map

The navigation bar is defined in `_layouts/default.html`. Each link points to a Markdown file in the repo root (Jekyll serves it as `.html` on the live site).

| Nav area | Link on site | Source file | Purpose |
|----------|--------------|-------------|---------|
| **Home** | `/` | `index.md` | Homepage; shows the most recent news teasers |
| **Calendar** | `/Calendar.html` | `Calendar.md` | Important dates, club times, holidays |
| **News archive** | `/News.html` | `News.md` | Full list of news posts (newest first) |
| **Club pictures** | `/Club.html` | `Club.md` | Photo galleries by year |
| **The Club** | `/Excelsior_Fencing_Club.html` | `Excelsior_Fencing_Club.md` | About the club |
| **Coaches** | `/Coaches.html` | `Coaches.md` | Coach bios, photos, contact emails |
| **Board of Directors** | `/Board_of_Directors.html` | `Board_of_Directors.md` | Board listing |
| **General information** | `/General_information.html` | `General_information.md` | Program overview |
| **Introduction to fencing** | `/Intro_to_Fencing.html` | `Intro_to_Fencing.md` | Beginner information |
| **Development & Recreation** | `/Development_and_Recreation.html` | `Development_and_Recreation.md` | Recreational programming |
| **Competition** | `/Competition.html` | `Competition.md` | Competitive programming |
| **Buying** | `/Buying.html` | `Buying.md` | Equipment purchasing guidance |
| **Rental** | `/Rental.html` | `Rental.md` | Equipment rental |
| **Links** | `/Links.html` | `Links.md` | Curated external links |
| **Find Us** | `/Find_us.html` | `Find_us.md` | Location and contact |
| **Register** | (external) | — | WellnessLiving login; not edited in this repo |

**Other root pages** (linked from content, not all in the nav table):

| File | Typical use |
|------|-------------|
| `The_History_of_Fencing.md` | Historical / educational content |
| `Club_times_*.md` under `News/` | Shared schedule snippets included by `Calendar.md` |

**Images:** `images/` (logo, banner, coach photos under `images/coaches/`). Use site-root paths like `/images/Excelsior-logo.png` in frontmatter.

---

## Repository layout (quick reference)

```
Excelsior-fencing-website/
├── _config.yml              # Jekyll theme and plugins
├── _layouts/default.html    # Site chrome, nav, CSS
├── CNAME                    # Custom domain (excelsiorfencing.ca)
├── index.md                 # Homepage + recent news includes
├── News.md                  # News archive
├── Calendar.md              # Calendar page
├── Coaches.md               # Coach profiles
├── …other *.md pages…       # One file ≈ one site page
├── News/
│   ├── YYYY/MM/DD/          # Individual news posts
│   │   ├── index.md         # Post page wrapper
│   │   └── content.md       # Post body
│   ├── Club_times_intro_and_rec.md   # Shared schedule (included)
│   ├── Club_times_competition.md
│   └── 2026/holidays.md              # Year-specific holidays
├── Club/                    # Club photo galleries by year
├── images/                  # Static images
└── Updating-the-website.md  # Maintainer guide (excluded from Jekyll build)
```

---

## Common editing tasks

### 1. Publish a news post

News posts live in dated folders: `News/YYYY/MM/DD/`.

**Step A — Create the post folder**

`News/2026/06/15/content.md` — the article body:

```markdown
## Headline here

Body text…

###### Posted: 2026-06-15
```

`News/2026/06/15/index.md` — page wrapper:

```markdown
---
image:
  path: /images/Excelsior-logo.png
  type: image/png
  alt: Excelsior Fencing Club
description: Short summary for search engines
site_name: Excelsior Fencing Club
title: Same as headline
---

{% include_relative content.md %}
```

**Step B — Wire it into the homepage and archive**

Add a teaser block at the **top** of both `index.md` and `News.md`:

```markdown
[link](News/2026/06/15/)
{% include_relative News/2026/06/15/content.md %}

---
```

The `[link](News/2026/06/15/)` line becomes a “read more” link to the full post page.

**Step C — Merge to `main`** (see GitHub workflow below). The site usually updates within a few minutes.

**Tip:** Match the tone and formatting of neighbouring posts in the same month.

---

### 2. Update the calendar or club times

`Calendar.md` does not duplicate schedule text. It **includes** shared files:

```markdown
{% include_relative News/Club_times_intro_and_rec.md %}
{% include_relative News/Club_times_competition.md %}
{% include_relative News/2026/holidays.md %}
```

Edit the included file(s) when times or holidays change. If a new calendar year starts, add something like `News/2027/holidays.md` and update the include path in `Calendar.md`.

---

### 3. Update coach information

Edit `Coaches.md`:

- Each coach is an HTML **table row** with bio text, `mailto:` link, and photo.
- Photos live in `images/coaches/`.
- **Coaching alumni** at the bottom of the page — add names only with board approval.
- Public coach list may differ from internal volunteer/VSC lists; verify before publishing.

---

### 4. Edit an ordinary page

Open the relevant root `.md` file (e.g. `Buying.md`, `Find_us.md`), change the Markdown below the frontmatter, and merge to `main`. Preserve existing frontmatter unless you intentionally change the page title or SEO description.

---

### 5. Add or replace images

1. Add the file under `images/` (or `images/coaches/` for coach photos).
2. Reference it with a site-root path: `/images/your-file.jpg`
3. Commit the image file together with the Markdown that references it.

---

## Using GitHub to publish changes

### Overview

```
edit on a branch → open Pull Request → review → merge to main → GitHub Pages rebuilds the site
```

Only changes merged to **`main`** appear on https://www.excelsiorfencing.ca.

### Option A — GitHub web interface (simplest)

Good for small text edits when you do not have a local clone.

1. Open https://github.com/Excelsior-Fencing-Club/Excelsior-fencing-website
2. Navigate to the file (e.g. `Coaches.md` or `News/2026/06/10/content.md`)
3. Click the **pencil (Edit)** icon
4. Make your changes
5. Choose **“Create a new branch for this commit and start a pull request”**
6. Name the branch (for news, a date like `2026-06-15` is common)
7. Click **Propose changes**, then **Create pull request**
8. Add a short summary of what changed
9. After review (or self-merge if you have permission), click **Merge pull request**

### Option B — Local clone (recommended for news posts and images)

1. **Clone** (once):

   ```bash
   git clone https://github.com/Excelsior-Fencing-Club/Excelsior-fencing-website.git
   cd Excelsior-fencing-website
   ```

2. **Update** before starting work:

   ```bash
   git checkout main
   git pull origin main
   ```

3. **Create a branch**:

   ```bash
   git checkout -b 2026-06-15-my-news-post
   ```

4. **Edit files**, then commit:

   ```bash
   git add .
   git status          # review what will be committed
   git commit -m "Add news post for June 15"
   ```

5. **Push and open a PR**:

   ```bash
   git push -u origin 2026-06-15-my-news-post
   ```

   GitHub will offer a link to create a pull request. Merge when ready.

### Pull requests — what to include

- **Title:** Clear one-line summary (e.g. “News: coach away June 19”)
- **Description:** What changed and why; mention if calendar/coaches/homepage were updated together
- **Checks:** GitHub Pages may run a build; fix any reported Jekyll errors before merging

### After merging

- Open https://www.excelsiorfencing.ca and confirm the change (hard refresh if needed: Ctrl+F5)
- Build status: repo **Settings → Pages** or the **Actions** tab if workflows are enabled

---

## Local preview (optional)

### Obsidian

Open the repo folder as an Obsidian vault. Useful for drafting Markdown and news posts. Obsidian preview does **not** run Jekyll — layout and `{% include_relative %}` tags will not match the live site exactly.

### Jekyll (closest to production)

Requires Ruby and Bundler. From the repo root:

```bash
bundle install
bundle exec jekyll serve
```

Then open http://localhost:4000. This runs the same Jekyll processing GitHub Pages uses (theme + includes).

---

## Jekyll features used on this site

| Feature | Example | Used for |
|---------|---------|----------|
| `{% include_relative path %}` | `{% include_relative News/2026/06/10/content.md %}` | News teasers on home/archive; calendar snippets |
| Frontmatter | `title`, `description`, `image` | SEO (`{% seo %}` in layout) and social previews |
| Remote theme | `_config.yml` | Base “hacker” styling via `assets/css/style.css` |

Avoid renaming `_layouts/default.html` or `_config.yml` unless you understand the impact on the whole site.

---

## Checklist before merging

- [ ] Public copy only — no internal club documents or personal data that should stay private
- [ ] News posts: `content.md`, `index.md`, **and** updates to top of `index.md` + `News.md`
- [ ] Calendar changes: edited the **included** snippet files, not just `Calendar.md` headings
- [ ] Coach changes: photo added to `images/coaches/` if new
- [ ] Links tested (especially external registration and mailto links)
- [ ] `###### Posted: YYYY-MM-DD` footer on new news posts

---

## Getting help

- **Site structure / this guide:** issue tracker in either repo; club issue [#155](https://github.com/Excelsior-Fencing-Club/Excelsior-Fencing-Club/issues/155) tracks website documentation
- **GitHub basics:** [GitHub Docs — Pull requests](https://docs.github.com/en/pull-requests)
- **Jekyll on GitHub Pages:** [GitHub Docs — GitHub Pages and Jekyll](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll)

---

*Last updated: 2026-06-27*
