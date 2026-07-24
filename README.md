# Welcome to Fletcher Kelly's Blog

![Website Build and Deploy](https://github.com/fskelly/me.fskelly.com/actions/workflows/hugo.yaml/badge.svg)

Hello and welcome to my blog! I'm Fletcher Kelly, a passionate tech enthusiast and lifelong learner. Here, I share my journey through the fascinating world of technology, home automation, and 3D printing. Whether you're a seasoned professional or just starting out, I hope you'll find something valuable and inspiring in my posts.

## What You'll Find Here

- **Home Automation:** Tips, tutorials, and projects on how to automate your home using tools like Home Assistant, ESPHome, and various smart devices.
- **3D Printing:** Insights into 3D printing, including reviews, tutorials, and projects using Fusion 360 and other design tools.
- **Tech Tutorials:** Step-by-step guides on various tech topics, from setting up servers to programming and beyond.
- **Personal Projects:** A peek into my personal projects and experiments, where I explore new technologies and share my findings.

## Join the Journey

I'm excited to share my knowledge and experiences with you. Feel free to explore, comment, and connect with me on [GitHub](https://github.com/fskelly), [Twitter](https://twitter.com/fskelly), and [LinkedIn](https://www.linkedin.com/in/fletcherkelly). Let's learn and grow together!

Happy reading!!  

Backend for my [blog](https://me.fskelly.com/)

## Hugo installation

I use the extended Hugo build on Windows.

```powershell
choco install hugo-extended -y
```

Or with winget:

```powershell
winget install -e --id Hugo.Hugo.Extended
```

If `hugo` is still not available after installing, open a new terminal session and run the version check again.

Verify the installation:

```powershell
hugo version
```

## Run the site locally

Start the local development server and include draft posts:

```powershell
hugo server -D
```

Build the production output into the `public/` folder:

```powershell
hugo --minify
```

## Create a new post

Posts are stored by year under `content/posts/`.

```text
content/
    posts/
        2026/
            my-new-post/
                index.md
```

Create a new draft post:

```powershell
hugo new posts/2026/my-new-post/index.md
```

New posts are created from the archetype with `draft = true`.

## Work with drafts

Preview draft content locally:

```powershell
hugo server -D
```

Publish a post by changing the front matter in the post file:

```toml
draft = false
```

## Publish changes

Build locally before pushing:

```powershell
hugo --minify
```

Commit and push the update:

```powershell
git add .
git commit -m "Add or update blog content"
git push origin main
```
