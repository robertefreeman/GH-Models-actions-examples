# The Sales Guy Who Accidentally Built AI Agents (Kinda)

I'm not a software developer anymore—I'm just your run-of-the-mill Federal Sales Director who happens to own 20 Raspberry Pis, more servers than I'd admit to my wife, and a delightfully clicky mechanical keyboard that makes me *feel* like a real developer.

I'm basically the beige of the engineering world and the participation trophy of the sales team. But, hey, I'm the coding Gandalf of the sales crew, and if the engineers ever had to sell a paperclip, I'd be their Wolf of Wall Street... of paperclips. I mention this to set the stage for the little adventure I went on today. This isn't an open-source project that's going to get forked all over the place and spawn product after product. This is just a handful of toys I built—with the help of GitHub Copilot—in a little under an hour. They work, and they demonstrate an idea that can be massively expanded on... by someone else.

So, with that said, let's get back to the story.

Recently, I was sitting in a product roadmap meeting—well, I was actually at home, but virtually with 100 of my closest friends. These meetings are my happy place at GitHub: lots of tech, lots of demos, and usually open-ended on their potential execution. I like to use my odd career background to reverse-engineer our new features into value for our customers—maybe spotting things others aren't. At the end of the meeting, I posted a quick set of bullets to an internal Slack, highlighting what I thought were the "sleeper" features—the ones that only got a brief mention but could deliver an outsized benefit. One of those was GitHub Models.

For those not familiar, GitHub Models is an AI inference capability on the GitHub platform that you can use to prototype AI features, either via an AI playground or an OpenAI-compatible API endpoint. It's a really fast way to weave AI into a product as you work through development and testing.

But that’s not the use case I had in mind. I'm thinking: GitHub Models here, GitHub Actions there, AI capabilities everywhere. My mechanical keyboard is going *click-clack-click-clack* as I start sketching out a framework to feed into GitHub Copilot chat.

## The Dangerous Art of Overly Technical Salesperson Logic

See, engineers think in elegant architectures and best practices. Me? I think in duct tape and "good enough for a demo." So I started mashing GitHub Models into GitHub Actions to see what was possible (if I gave myself 60 minutes or less).

Armed with my clicky keyboard, GitHub Copilot (my new best friend, who makes me look way smarter than I am), and the kind of confidence that comes from not knowing what you don't know, I decided to see what I could pull off. Not what was planned. Not what was best practice. Just... possible.

## Building Backwards from "What If"

The beauty of not being a real developer is that you don’t know what you’re not supposed to do. So, when I started combining GitHub Models and Actions, my sales brain immediately thought: "AI Agent"... because that's what sales brains do—lock onto the buzziest word around and ride it until something new comes along. And right now, nothing is buzzier than AI Agents.

What emerged from my keyboard-clacking wasn’t sophisticated. Think less "enterprise-grade AI platform" and more "digital interns who surprisingly show up to work." But that’s exactly the point.

So I built four example action workflows and tossed them all into a GitHub repo, available for anyone who wants to play around with them.

1. **Pull Request Summarization Action:** This workflow reads pull requests (PRs) and uses an AI Model to write a description that actual humans might understand. Is it revolutionary? No. But seeing GitHub Actions start “thinking” and demonstrating the ability to perform complex tasks with minimal code felt like accidentally discovering your calculator can write poetry.

2. **Code Complexity Evaluation Action:** If I'm going to play developer for the day, I might as well build something that judges how well other people play developer. It's essentially that coworker who passive-aggressively points out when your code is getting a bit too creative. Built entirely from curiosity (and a little bit of spite). This action reviews any JavaScript files and evaluates how "complex" they are (it’s a toy—I let the AI decide what "complex" means).

3. **Project Summarization Action:** With each commit, this action updates a running log of how everything in a repo works, what each piece actually does, and where it’s all found. Why? Because it helps keep track of what’s going on in a codebase. I use files like this to improve Copilot’s performance on my larger projects. The idea is, I can include this file directly in a question or planning exercise, instead of having Copilot scan the whole repo every time I want to evaluate a small change.

And then I got a little over-eager.

## The Panda Cam Observer: Peak Salesperson Engineering

Apparently, I have no self-control—so I created "The Panda Cam Observer." Every thirty minutes, this digital wildlife enthusiast checks the National Zoo's panda webcam and tries to spot a panda. If one’s around, it provides a description of what the panda is doing. This action uses a multimodal model (images and text) to "see" if a panda is visible at the panda house and, if so, writes an update to a GitHub Pages-hosted website.

Why? Because sometimes, when you're exploring the art of the possible, you have to build something ridiculous to understand what’s actually practical. It's like how you test a sports car by seeing how fast it goes—not by checking if it can parallel park.

This absurd little creation became my favorite demonstration of possibility. "Look," I'd tell myself, "if I can make GitHub Actions watch pandas and report on their activities, imagine what real developers could build."

These "AI agents" are held together with virtual duct tape and wishful thinking. They're curl commands pretending to be sophisticated, JSON processing masquerading as intelligence, and a lot of fingers crossed. But they work. And more importantly, they show what's possible when you think less about what tools are supposed to do and more about what they could do.

## What This Means for Real Customers

The real revelation wasn’t that I’d built something amazing—I definitely hadn’t. It was that I’d built something at all. In about an hour. Using tools just sitting there, waiting to be combined in ways their creators might not have imagined.

That kind of accessibility excites me. Not because I want to become a developer (I really, really don’t), but because it means our actual developer users are going to do incredible things with these tools. If I can hack together AI agents between sales calls, imagine what people who actually know what they’re doing will create.

## The Beautiful Mess of Innovation

What started as me trying to understand our product roadmap by building backwards turned into something more interesting: a glimpse at how innovation really happens in the wild. Not through careful planning and structured development, but through curious people with clicky keyboards asking, "What happens if I connect this to that?"

My little experiments are embarrassingly simple, wonderfully hacky, and probably violate best practices I don’t even know exist. But they represent something important: the democratization of AI, to the point where even salespeople can build useful (or at least amusing) automations. That’s what excites me most about AI right now: it enables projects that, in the past, I wouldn’t have had the time or capability to execute. Now it’s a lunch break experiment, and then I can move on.

## AI Agents?

So did I build an AI Agent? Well, in its simplest form, an AI Agent is a software platform that performs a task independently. So **YES**—I’m going to say I built an Agent.

---

*Want to see what happens when salespeople play developer? Check out my delightfully amateur AI agents: [GH-Models-actions-examples](https://github.com/robertefreeman/GH-Models-actions-examples)*

#GitHub #Sales #AI #Innovation #ProductDiscovery #TechExploration #SalesEngineering #BuildingBackwards

























































































































































































































































## 🐼 Live Panda Cam Analysis

*This section is automatically updated every 30 minutes during zoo hours using AI-powered monitoring.*

**Last Updated:** 2025-06-25 15:31:45 UTC

**Status:** Maintenance  
**Reason:** The panda cam is currently undergoing scheduled maintenance or technical updates.  
**Recommendation:** Please check back later; the live feed should be available again soon.  
**Technical Note:** The status image indicates a grey background with red text stating \

---

*🤖 Powered by GitHub Actions + GitHub Models AI*

This automated system monitors the National Zoo panda webcam and provides intelligent status updates. When the live feed is unavailable, it creates informative status images and uses AI to analyze the current situation.

---

🔗 **Project Repository:** [github.com/robertefreeman/GH-Models-actions-examples](https://github.com/robertefreeman/GH-Models-actions-examples)

#GitHubActions #AI #WebcamMonitoring #Automation #GitHubModels #PandaCam #ComputerVision #DevOps
