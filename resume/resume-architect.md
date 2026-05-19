# ANOOP N P

**Kerala, India** · anoopnpgm@gmail.com · linkedin.com/in/anoopnadakkara · github.com/anoopnadakkara

---

## SUMMARY

Associate Technical Architect with 15+ years of experience designing and delivering scalable cloud-native enterprise systems. Specialises in microservices architecture, Azure cloud platforms, distributed systems, and platform modernisation. Proven track record leading end-to-end delivery from architecture through to production across EdTech, compliance, SaaS, and enterprise domains. Strong background in technical leadership, team mentoring, and cross-functional stakeholder engagement.

---

## CORE COMPETENCIES

**Architecture & Design** · Microservices · Domain-Driven Design (DDD) · Event-Driven Architecture · CQRS · Saga Pattern · Clean Architecture · SOLID · SOA · Strangler Fig Migration

**Cloud & DevOps** · Microsoft Azure (AKS · App Services · Service Bus · Blob Storage · Cosmos DB · Key Vault · Azure AD) · Docker · Kubernetes · KEDA · CI/CD · Azure DevOps · ARM Templates (IaC) · GitHub Actions · TeamCity · Octopus Deploy · Blue/Green Deployment

**Languages & Frameworks** · C# · .NET 5–8 · ASP.NET Core · Web API · Entity Framework Core · Blazor · SignalR · MassTransit · gRPC · React.js · TypeScript · JavaScript · T-SQL

**Messaging & Data** · RabbitMQ · Azure Service Bus · SQL Server · Cosmos DB · Elasticsearch · MongoDB

**Practices** · Agile/Scrum · TDD · Technical Mentoring · Architecture Reviews · Cross-Functional Leadership

---

## PROFESSIONAL EXPERIENCE

### Associate Technical Architect
**Techversant Infotech, India** · Sep 2025 – Present

- Architecting a cloud-native SaaS proctoring application — system design, microservices boundaries, Azure infrastructure, and scalability planning for a multi-tenant examination proctoring platform.
- Leading technical evaluation and integration architecture for a payment integration initiative enabling high-value transactions within a trust application — vendor assessment, security model, and integration design.
- Defining architectural standards, conducting design reviews, and aligning implementation teams with architectural intent.
- Mentoring development teams on distributed system patterns, Azure cloud practices, and microservices design.

---

### Career Break — Personal & Professional Development
**Nov 2024 – Aug 2025**

- Authored 15 detailed technical case studies documenting architecture decisions, design patterns, and measurable outcomes across major project deliveries.
- Built a professional portfolio website and GitHub portfolio to support consulting and architect-level engagements.
- Focused on architecture upskilling, cloud-native patterns, and professional development.

---

### Technical Lead → Senior Technical Lead (Architect)
**Orion Innovations, India** · 2020 – Nov 2024

- Architected and implemented a compliance-grade engagement archival system — all data ingested exclusively via the engagement system's Web API, packaged into AES-256 encrypted `.retx` archives stored in tenant-scoped Azure Blob containers.
- Designed an event-driven archival pipeline using Azure Service Bus (choreography-based saga) — fully async and decoupled from live engagement workflows with zero performance impact.
- Built a separate licensed viewer application (WinForms + CefSharp) with tenant isolation, version compatibility management, and SHA-256 integrity verification.
- Designed multi-layer security — per-tenant Blob access policies (JWT claims), AES-256 encryption with Azure Key Vault key management, and viewer license validation.
- Led Scrum delivery, mentored team members, and conducted architecture and code reviews.

**Key Achievement:** Delivered government-regulatory-compliant archival solution with 99.9% uptime, zero live system impact, and full tenant data isolation.

---

### Technical Lead
**RM Education, India** · 2015 – 2020

- Led end-to-end delivery across the full Digital E-Marking Platform ecosystem — administration interface, platform modernisation, DevOps transformation, scanning automation, and document conversion subsystem.
- **Platform Modernisation:** Led Strangler Fig migration of WCF/Silverlight monolith to cloud-native microservices with React.js frontend — decomposed into 7 domain-driven services each with independent database schemas. Zero downtime throughout.
- **Document Conversion Service:** Re-architected sequential file conversion bottleneck into parallel format-specific worker pools (ImageMagick, FFmpeg, LibreOffice, Ghostscript, Chromium Headless) with KEDA queue-depth autoscaling — reduced marking pipeline start time by **91%** (45 min → 4 min on 5,000-file batches).
- **DevOps Transformation:** Designed CI/CD pipelines (TeamCity + Octopus Deploy → Azure DevOps YAML), ARM template IaC, blue/green deployments with automated rollback, and full secrets migration to Azure Key Vault. Reduced time-to-production from hours to under 30 minutes.
- **Scanning Automation:** Contributed to architecture and led development of distributed scanning system — configurable Elsa Workflow pipelines per exam type (OMR, descriptive, hybrid), RabbitMQ + MassTransit async ingestion, Scantron SDK abstraction.
- **Administration Interface:** Designed and delivered the Zoning Module — interactive jQuery canvas tool enabling exam coordinators to split candidate scripts into independently assigned answer zones for specialist marker pools.
- Managed Scrum ceremonies, sprint delivery, offshore client go-live support, and cross-functional team coordination.

**Key Achievements:**
- 91% reduction in marking pipeline start time through parallel processing re-architecture
- 30% infrastructure cost reduction via cloud migration and cold data decoupling
- 99.9% uptime post-migration on AKS with horizontal pod autoscaling
- Zero-downtime platform modernisation of a business-critical exam marking system
- Sub-30-minute merge-to-production pipeline reduced from hours of manual coordination

---

### Senior Software Engineer → Lead Developer
**ISPG Technologies, India** · 2011 – 2015

- Led end-to-end design and delivery of a custom social networking Bible study platform — XML content processing pipeline supporting OSIS, ThML, and USX standards with XSLT transformations, extended OSIS specification, and verse-level social interactions (likes, bookmarks, comments, sharing).
- Built a location-aware Business Directory and Coupons & Promotions Platform using Elasticsearch geo-spatial search, Google Maps API, and subscription-tier premium placement via Elasticsearch function-score queries.
- Delivered two full-stack e-commerce platforms (Ayurvedic cosmetics and health & wellness) with promotional rule engines, bundle detection, optimistic concurrency on discount codes, and payment gateway integration.
- Designed Business Process Automation systems — donation management platform (multi-tenant, campaign lifecycle, donor analytics) and wood veneer factory system (per-sheet stock traceability, conversion yield analytics, client showcase portal).
- Progressed from Senior Software Engineer to Lead Developer — taking full end-to-end ownership of product delivery.

---

### Software Engineer → Senior Software Engineer
**Fies Systems, India** · 2008 – 2009

- Contributed to development and enhancement of a government back-office management system for a police department — crew management, financial aid approval workflows, operational activity tracking, and centralised audit logging.
- Contributed to a large-scale retail ERP system — warehouse operations, inventory management, billing workflows, and POS terminal integration across a multi-location retail chain.
- Built core modules including configuration-driven approval chain routing, field-level audit trail interceptor, and server-side paging on large operational datasets.

---

## TECHNICAL SKILLS SUMMARY

| Category | Technologies |
|---|---|
| Languages | C#, T-SQL, TypeScript, JavaScript, XML/XSLT |
| Frameworks | .NET 5–8, ASP.NET Core, Web API, EF Core, Blazor, MassTransit, gRPC, SignalR |
| Cloud | Azure AKS, App Services, Service Bus, Blob Storage, Cosmos DB, Key Vault, Azure AD |
| DevOps | Azure DevOps, Docker, Kubernetes, KEDA, ARM Templates, TeamCity, Octopus Deploy |
| Messaging | RabbitMQ, Azure Service Bus, MassTransit |
| Databases | SQL Server, Cosmos DB, MongoDB, Elasticsearch |
| Architecture | Microservices, DDD, Event-Driven, CQRS, Clean Architecture, Saga, Strangler Fig |
| Frontend | React.js, Blazor, Razor Components, jQuery |
| Practices | Agile/Scrum, TDD, CI/CD, IaC, Technical Mentoring |

---

## KEY ACHIEVEMENTS

- **91% reduction** in marking pipeline start time — parallel format-specific worker pools with KEDA autoscaling
- **30% infrastructure cost reduction** — cloud migration decoupling cold data from live systems
- **99.9% uptime** post cloud migration on AKS with horizontal pod autoscaling
- **5M+ users** supported across distributed systems with 70% performance improvements
- **Zero-downtime** WCF/Silverlight to microservices modernisation using Strangler Fig pattern
- **Sub-30-minute** merge-to-production pipeline reduced from hours of manual coordination

---

## EDUCATION

**Bachelor of Technology (B.Tech) — Electronics & Communication Engineering**
Kannur University, Kerala, India

---

## AREAS OF EXPERTISE

Solution Architecture · Cloud-Native Architecture (Azure) · Microservices & Distributed Systems · Platform Modernisation & Legacy Migration · DevOps Transformation & IaC · High-Throughput Data Processing · Technical Leadership & Mentoring · Compliance & Security-Grade System Design · Agile Delivery · SaaS Product Architecture · Payment Systems Integration

---

## ADDITIONAL

- **Location:** Kerala, India — open to remote roles globally
- **Availability:** Immediately available for architect, consultant, and advisory roles
- **Portfolio:** github.com/anoopndakkara
- **Case Studies:** 15 detailed project case studies at [portfolio](https://github.com/anoopnadakkara/professional-profile/blob/main/README.md)