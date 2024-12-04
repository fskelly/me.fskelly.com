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

## HUGO installation

I use [chocolatey](https://chocolatey.org/install) as my package manager or installation engine.

Installing HUGO is easy, I choose the extended version to allow for more capabilities.

```powershell
choco install hugo-extended -y
```

My build command

```bash
C:\ProgramData\chocolatey\lib\hugo-extended\tools\hugo.exe
```

## Create a new post

I like to create my content based upon year  
My folder structure looks like this  

```bash
content  
|---posts
    |---year
        |---postTitle
            |---index.md
```

```bash
hugo new posts/{{year}}/{{postTitle}}/index.md
```
