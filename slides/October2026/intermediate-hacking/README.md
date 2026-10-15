# Intermediate Hacking — One Tunnel, Two Stories

Claes “kryssar” Gyllhamn · Malmö 2600 · 2 October 2026

A lab story about how a compromised public web server can expose internal data and lead toward greater control of a workstation. The second half follows the same activity from the defender’s perspective.

## Presentation files

- [Slides as PDF](slides.pdf): 32 audience slides, without presenter notes.
- [Editable PowerPoint](slides.pptx): the same slides, without presenter notes.
- [Companion script](script.html) (<a href="script.md" download>Markdown</a>): a short, plain-language explanation for every slide, with the management and defensive implications.
- [Demo video](demo.mp4): the original 15.6-second recording, in 1080p H.264 MP4. It has no audio.
- [Video captions](demo.vtt): an optional explanation of the demonstrated outcome.

At slide 31, open **demo.mp4**, then return to slide 32. Video is supplied separately so playback does not depend on PowerPoint media support or Google Drive access. The poster image in the deck also links to the original Drive recording, which requires access to that file. PDF does not play the video internally.

Download this folder together to view the slides and play the clip offline. Repository previews may offer a download instead of inline video playback.

## What the scenario demonstrates

Network reachability, permission to read information, and operating-system authority are separate controls. An allowed connection can expose another service, but a separate authorization failure exposes its private data. A separate local trust failure permits a privileged process on the tested workstation.

The presentation uses a controlled lab and a narrated incident storyline. The network zones describe roles in that scenario. The SYSTEM result applies to the tested Windows 10 Pro build 19045 environment, while the Server 2019 test did not show the same authority change. It is not a claim about every Steam installation. The data example shows one private record, not an entire database.

## Reuse

Keep the slides, script, and video together so the explanation and these limits travel with the demonstration.
