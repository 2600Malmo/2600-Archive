# Intermediate Hacking — One Tunnel, Two Stories

## Companion script

Claes “kryssar” Gyllhamn · Malmö 2600 · 2 October 2026

These short explanations follow the 32 slides in the audience edition. Each opens with the main point, followed by language suitable for a general audience or a security leadership discussion.

This is a controlled lab story. Some events connect the narrative, while the network and process evidence establish specific results. The private-data example concerns one record. The SYSTEM result concerns the tested Windows 10 environment, not every installation of the software shown.

## Slide 01 — Intermediate Hacking

**A small breach can have consequences well beyond the first machine.**

We follow a compromised public web server toward private information and greater control of a workstation. Then we revisit the activity through the defender’s eyes. The central question is how each system’s connections and permissions affect the damage an attacker can cause.

## Slide 02 — Claes // kryssar + Codex

**This presentation combines hands-on security work with an AI build partner.**

I’m Claes, also known as kryssar, a security engineer in Malmö. I build labs that let us examine both attacks and defenses. Codex helped with the build and presentation. The purpose is to turn a technical demonstration into lessons people can understand and use.

## Slide 03 — What makes this intermediate?

**The useful skill is understanding relationships and checking assumptions.**

Security work involves observing what happens, considering possible explanations, and checking which explanation the evidence supports. A successful command alone tells us very little about overall risk. We need to understand what access changed and what that change makes possible.

## Slide 04 — One breach becomes an internal attack path

**One compromised service can expose several business risks.**

The story begins at a public web server and splits into two branches. One concerns private application data. The other concerns control of a developer’s workstation. These outcomes depend on further weaknesses and trust relationships. The first breach creates an opportunity rather than automatically compromising everything.

## Slide 05 — Outside, DMZ, inside

**Network boundaries matter only when the permitted connections support them.**

A DMZ is the area intended to separate public services from internal systems. The diagram shows the systems’ roles in our lab story. Focus on which machines may communicate and why. Malcolm observes network activity, while Sysmon records activity on Windows. Neither is an attacker stepping stone.

## Slide 06 — One click. One delivery route.

**An ordinary workflow can introduce untrusted software.**

The story uses a familiar user action to explain how a file reaches the web server and runs. The captured network evidence begins with the file transfer. For management, the lesson is to examine how software enters an environment and who or what is allowed to execute it.

## Slide 07 — The file crosses the Internet

**A file transfer becomes significant when it changes what a system can do.**

The lab shows the web server receiving an executable from the tool host. The diagram represents delivery across an external boundary. Investigators can use the source, destination, and file information to establish what moved. They must then connect delivery to evidence of execution.

## Slide 08 — Defacement would be the easy ending

**Visible disruption may be only a small part of the exposure.**

A changed website is obvious. Access to the systems behind it may be more consequential. After a public service is compromised, the response needs to consider what that service can reach and what other systems trust it to do. Restoring the website alone may leave those questions unanswered.

## Slide 09 — Execution is not a route

**Outbound connections belong in the security review too.**

In the scenario, the attacker cannot simply connect inward. The compromised server can still initiate an outward connection. That permitted direction becomes important to the incident. Blocking unsolicited inbound traffic addresses only part of the communication that a compromised system might use.

## Slide 10 — DVWA calls outward; access comes back

**A permitted connection can carry traffic with an unexpected purpose.**

A tunnel carries other communication inside an existing connection. Here, the web server initiates the connection outward, and the attacker uses it to interact with systems the server can reach. The leadership question is whether outgoing traffic has a justified purpose and whether unusual use becomes visible.

## Slide 11 — The tunnel introduced itself

**Network records can expose behavior that deserves investigation.**

The observed connection includes protocol information associated with the tunneling tool. That gives defenders a useful clue. The broader signal is a public web server making an unusual outward connection. A detection strategy should also consider behavior because a literal tool name may not always appear.

## Slide 12 — Hacktop chooses; DVWA originates

**A familiar internal source is not proof of a trustworthy action.**

The attacker directs the activity, but the compromised web server originates the internal connections. A receiving system therefore sees the web server as its network counterpart. This is why an internal address alone cannot establish who is acting or whether their request deserves access.

## Slide 13 — Root changes what DVWA can tell us

**Greater privileges can expose more information about the environment.**

Root is the highly privileged Linux account. In this part of the scenario, control at that level allows observation of traffic visible to the web server. Existing conversations reveal useful relationships. This illustrates why unnecessary privileges increase the consequences of a compromise.

## Slide 14 — Why reverse SOCKS?

**One communication channel can serve more than one destination.**

SOCKS is a way to relay network connections. The slide compares the scope of different connection methods. The general lesson is that seeing one outward connection does not necessarily mean only one internal system is involved. Investigators need to understand the activity carried through it.

## Slide 15 — We test the leads—not the subnet

**A service answering a request establishes reachability, not permission.**

The observations identify an internal application and a Windows management service. A response confirms that a network path exists. It does not establish a successful login or administrative control. Keeping those distinctions clear prevents both exaggerated incident reports and false confidence in existing protections.

## Slide 16 — SOCKS scouts; a fixed forward holds the door

**A temporary discovery path can become repeatable access.**

The slide distinguishes a flexible relay from a connection tied to one service. Both depend on the compromised server’s network position. For defenders, the important question is whether an unexpected connection has created continuing access to a sensitive system and how to contain it.

## Slide 17 — Why the auction server?

**Normal application relationships can reveal where valuable information lives.**

The web server’s existing communication makes the auction service relevant to the story. The tunnel provides a route to it. Permission to read its data remains a separate decision for the application. Network controls and application access checks therefore protect different parts of the same path.

## Slide 18 — The message reaches a private object

**Finding a record must not be enough to read it.**

The application returns a private object without checking whether the requester has permission. This is an authorization failure, known as Broken Object Level Authorization. A system must enforce access to each requested record. Being reachable on the network cannot substitute for that check.

## Slide 19 — The private record comes back to Hacktop

**The demonstrated impact is disclosure of one private record.**

Information travels from the internal application, through the compromised server, to the attacker’s machine. That turns a missing access check into a confidentiality incident. The example establishes a specific disclosure. It does not demonstrate that the attacker copied the entire database.

## Slide 20 — The developer has to reach the web service somehow

**Administration paths can connect systems with very different levels of exposure.**

Developers and administrators need legitimate ways to maintain services. The storyline uses that operational relationship to introduce the workstation branch. Security reviews should examine the permitted direction of management access and whether a compromised public service can reach the people or systems that maintain it.

## Slide 21 — The foothold reveals a Windows management surface

**An exposed management service increases the importance of identity controls.**

WinRM is a Windows remote-management service. Its response in this example establishes that the service is reachable from the compromised server. Authentication is still a separate boundary. The evidence at this point does not establish that the attacker has logged in.

## Slide 22 — A name-resolution leak becomes authenticated access

**Weaknesses around identity can make a reachable service more dangerous.**

The scenario illustrates how network name lookup behavior exposes authentication material and how a recoverable password can turn that exposure into account access. The password is not simply sent as readable text. The defensive lesson concerns the combination of legacy authentication behavior, password strength, and access to management services.

## Slide 23 — The cracked identity opens the workstation

**Access to a user account and administrative authority are different outcomes.**

The storyline now follows access under a developer identity. The displayed account context has standard-user permissions. That distinction matters: an account compromise can already be harmful, but further control depends on additional permissions or a separate weakness. Incident reports should state exactly which level of access the evidence supports.

## Slide 24 — A developer identity influences a privileged service

**Software running with high privileges creates a critical trust boundary.**

The lab illustrates a service that accepts user-influenced input and starts a process with SYSTEM authority. The broader concern is which installed programs run with elevated permissions and what inputs they trust. Software approval, patching, and least privilege each help reduce this exposure.

## Slide 25 — SYSTEM

**The demonstrated process has powerful local operating-system authority.**

SYSTEM is a highly privileged Windows identity. The result shows that the trust boundary failed in the tested workstation environment. It does not by itself prove control of the organization’s domain or every other machine. The important evidence is the process identity and how it obtained that authority.

## Slide 26 — Sysmon records the authority jump

**Endpoint evidence helps explain how the privilege change happened.**

Sysmon records process activity on Windows. The events connect a user context, a privileged service, and a child process running as SYSTEM. The result occurred in the Windows 10 Pro build 19045 lab, while the Server 2019 test did not show the same change. Environment and software configuration matter.

## Slide 27 — Rewind the incident

**Defenders must assemble a story from incomplete observations.**

The audience has followed an orderly narrative. A security team usually receives separate connection records, file events, and process activity. Its job is to connect those observations, identify affected systems, and decide what to contain. Useful evidence must explain the incident well enough to support action.

## Slide 28 — Blue reconstructs the pivot

**Related events can explain more than an isolated alert.**

The file transfer, outward connection, internal activity, and private response become meaningful when linked by time and system identity. This reconstruction explains how the compromised server became a bridge. It also helps defenders identify which connections and systems need attention during containment.

## Slide 29 — 1,115 alerts. Five events tell the story.

**Alert volume is a poor substitute for an accurate incident picture.**

In this lab, one sensor produced 1,115 checksum alerts, while five linked events explained the main network story. These numbers describe this demonstration, not a universal ratio. The management lesson is to evaluate whether monitoring produces usable evidence and timely decisions, rather than rewarding a large alert count.

## Slide 30 — The commands change. The questions transfer.

**The lasting lesson is to understand and limit trust.**

Ask what each system may reach, which information a user may access, and what privileged software will accept from them. Review allowed traffic, keep systems and applications updated, and control software installation. Those measures address different failures in the story. Monitoring then helps establish when a boundary has been crossed.

## Slide 31 — Demo or die

**Watch the process identity and the workstation context.**

Play [demo.mp4](demo.mp4). The silent clip lasts about 16 seconds and shows the lab’s SYSTEM process on the Windows workstation. It illustrates the authority outcome discussed in the preceding slides. The short recording alone does not document every earlier step in the incident story. Return to the closing slide afterwards.

## Slide 32 — Join us

**Good security work includes making the lesson understandable to others.**

Thank you for following the story. The closing slide provides contact and careers links for anyone interested in the work. For discussion, consider which boundary in your own environment would limit a similar incident and what evidence would tell you whether it held.
