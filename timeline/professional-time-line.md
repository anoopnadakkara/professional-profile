# Professional Journey — Anoop N P

> 15+ years building enterprise software — from writing first lines of production code to architecting distributed cloud-native systems serving millions of users.

---

## Career Progression at a Glance

```
Software Engineer
      │
      ▼
Senior Software Engineer
      │
      ▼
Lead Developer
      │
      ▼
Technical Lead
      │
      ▼
Senior Technical Lead (Architect)
      │
      ▼
Associate Technical Architect  ◄── Present
```

---

## Timeline

---

### 🟢 2009 — Career Begins
**Role: Software Engineer**
*First steps into enterprise software development on the .NET stack*

- Joined as a Software Engineer working on large-scale enterprise systems.
- Contributed to a **Web CRM System** — lead management, sales pipeline, activity logging, and ERP-integrated sales order generation. First exposure to full sales lifecycle software and ERP integration patterns.
- Contributed to a **Retail ERP System** — warehouse operations, inventory management, billing workflows, and POS terminal integration across a multi-location retail chain. Worked with RabbitMQ, gRPC, and Web API for real-time inventory sync between POS hardware and the ERP backend.

**Technologies:** .NET Framework · ASP.NET · C# · SQL Server · jQuery · Web API · RabbitMQ · gRPC · Azure

---

### 🟡 2011 — First Specialisation
**Role: Senior Software Engineer**
*Growing ownership of complex modules within a government-grade system*

- Promoted to Senior Software Engineer.
- Contributed to a **Government Back Office Management System** for a police department — crew management, financial aid administration, operational activity tracking, and centralised audit logging.
- Designed a configuration-driven approval chain for financial aid workflows and implemented a field-level audit interceptor operating at the data access layer — first architectural thinking beyond feature code.
- Worked with Infragistics enterprise controls and SQL Server full-text search for large operational datasets.

**Technologies:** .NET Framework · ASP.NET · C# · SQL Server · jQuery · Infragistics Controls

---

### 🔵 2013 — Taking Ownership
**Role: Lead Developer**
*End-to-end ownership of product delivery across multiple business domains*

- Stepped into the Lead Developer role — responsible for architecture, delivery, and team guidance on full projects.
- Built a **Custom Social Networking Platform for Bible Study** — designed an XML content processing pipeline supporting OSIS, ThML, and USX Bible standards, extended the OSIS specification with custom platform elements, and built a jQuery-based interactive Bible reader with verse-level social interaction. First experience owning a complex content processing pipeline end to end.
- Delivered a **Wood Veneer Factory BPA System** — digitised manual operations including stock management, veneer conversion tracking, photo-based pattern identification, and a client-facing showcase portal.
- Delivered a **Donation Management Platform** — multi-tenant fundraising system with configurable theming, campaign lifecycle management, and donor engagement features.
- Built two **E-Commerce Platforms** — Ayurvedic cosmetics and health & wellness products — including payment gateway integration, promotional engines, AJAX cart, and order management pipelines.
- Built a **Business Directory Platform** and **Coupons Directory** — both featuring Elasticsearch geo-spatial search, Google Maps integration, and subscription-tier placement boost using Elasticsearch function-score queries. First hands-on experience with search engineering and location-aware discovery.

**Technologies:** .NET Framework · ASP.NET MVC · C# · jQuery · SQL Server · Elasticsearch · Google Maps API · Bootstrap · Payment Gateway · XML · XSLT

---

### 🟠 2017 — Enterprise Scale & Platform Thinking
**Role: Technical Lead**
*Leading teams, owning architecture, driving modernisation*

- Joined as Technical Lead on the **Digital E-Marking Assessment Platform** — one of the most technically complex and impactful engagements of the career.
- Led end-to-end delivery across four major workstreams over several years:

#### 2017–2018 — Administration Interface
- Took ownership of the **E-Marking Administration Interface** — the operational control centre for the entire marking ecosystem.
- Designed and delivered the **Zoning Module** — enabling exam coordinators to split candidate answer scripts into independently assigned answer zones using an interactive jQuery canvas tool. This became a core feature of the platform's response allocation pipeline.
- Led the Scrum team through the support and enhancement phase, resolving issues and delivering features without regression on active marking workflows.

#### 2018–2020 — Platform Modernisation
- Led the **full modernisation of the E-Marking Platform** from a WCF/Silverlight monolith to cloud-native microservices with a React.js frontend.
- Designed and executed an incremental **Strangler Fig migration** — zero downtime, no big-bang cutover, backward compatibility maintained for existing integrations throughout.
- Decomposed the WCF monolith into domain-driven microservices — Marker Management, Response Distribution, Marking Session, SLA Tracking, Statistical Analytics, Quality Assurance, and Result Consolidation — each with its own database schema.
- Introduced **RabbitMQ + MassTransit** for event-driven cross-domain communication and **gRPC** for latency-sensitive synchronous contracts.
- Delivered new modules — marker onboarding, SLA-based completion tracking, and statistical analytics — built greenfield on the modernised stack while legacy migration was in progress.

#### 2019–2020 — DevOps Transformation
- Led the **Cloud Migration & DevOps Transformation** initiative in parallel with platform modernisation.
- Designed and implemented end-to-end **CI/CD pipelines** using TeamCity and Octopus Deploy, migrated to **Azure DevOps YAML pipelines**, and defined all infrastructure as **ARM Templates (IaC)**.
- Implemented **blue/green deployment with automated health-probe rollback** — reduced time from merge to production from hours of manual coordination to under 30 minutes.
- Migrated all secrets from source control to **Azure Key Vault** — zero secrets in code across all services.

#### 2020–2021 — Scanning Automation
- Contributed to the architecture and led end-to-end development of the **Digital E-Marking Scanning Automation** system — a distributed microservices extension enabling universities to automate high-volume exam response scanning.
- Designed configurable **Elsa Workflow** pipelines per exam type (OMR, descriptive, hybrid), implemented **RabbitMQ + MassTransit** for async large-scale scan ingestion, and integrated Scantron SDK via an abstracted adapter layer.
- Participated in **offshore client implementation**, providing technical stabilisation and integration support during go-live.

**Technologies:** .NET · ASP.NET Core · C# · Microservices · RabbitMQ · MassTransit · gRPC · Docker · AKS · Azure DevOps · ARM Templates · TeamCity · Octopus Deploy · React.js · Elsa Workflows · SQL Server · Elasticsearch · Azure Monitor · Serilog

---

### 🔴 2021 — Architect-Level Ownership
**Role: Senior Technical Lead (Architect)**
*System design, cross-team technical governance, and high-impact delivery*

- Promoted to Senior Technical Lead with architect-level responsibility.

#### 2021 — Document Conversion Service *(Deep Technical Contribution)*
- Identified and solved a **critical bottleneck** in the marking pipeline — a sequential file conversion process that delayed marking start by hours on large exam runs.
- Re-architected the conversion pipeline into a **high-throughput parallel processing system** with format-specific worker pools (ImageMagick, LibreOffice Headless, FFmpeg, Ghostscript, Chromium Headless), independent RabbitMQ queues per format, and **KEDA queue-depth-driven autoscaling** on AKS.
- Reduced **time to first marker availability from ~45 minutes to ~4 minutes** on a 5,000-file batch — a 91% reduction.
- Introduced GPU node pools for video conversion, chunked streaming I/O for large file resilience, and per-file `ConversionComplete` events for partial availability — markers could begin as soon as the first files converted.

#### 2022–Present — Engagement Retention & Archiving Solution
- **Architected and implemented** a compliance-driven archival subsystem for an enterprise audit management platform.
- Designed an event-driven archival pipeline using **Azure Service Bus** with choreography-based saga pattern — fully async, decoupled from live systems.
- Built secure packaging with AES-256 encryption, SHA-256 integrity hashing, and Azure Key Vault key management. Introduced **Razor Class Library (build-time compiled)** for type-safe HTML generation in the embedded viewer after performance validation.
- Deployed all services as containerised microservices on **AKS** with independent horizontal scaling.

**Technologies:** .NET 6 · C# · Microservices · AKS · Azure Service Bus · Azure Blob Storage · CosmosDB · Azure Key Vault · Identity Server · Azure AD · Razor RCL · React.js · WinForms · CefSharp · FFmpeg · LibreOffice Headless · ImageMagick · Ghostscript · Chromium Headless · KEDA · Docker · Serilog · Azure Monitor

---

### 🟣 Present — Associate Technical Architect
**Role: Associate Technical Architect · Senior .NET Consultant**
*Bridging deep technical execution with system-wide architectural vision*

- Operating as **Associate Technical Architect** — responsible for system design, architectural governance, cross-team technical alignment, and mentoring.
- **Mentoring** implementation teams on overseas projects — providing remote architectural guidance, reviewing implementation against design intent, and ensuring microservice boundaries, integration contracts, and security patterns are correctly applied in delivery.
- Continuing to drive platform evolution on the E-Marking ecosystem with a focus on scalability, cloud cost optimisation, and observability maturity.

**Focus Areas:** Cloud-Native Architecture · Microservices · DDD · Azure · DevOps · Team Mentoring · Cross-Functional Technical Leadership

---

## Skills Evolution

| Period | Focus |
|---|---|
| 2009–2011 | .NET fundamentals · SQL Server · CRUD systems · ERP integration |
| 2011–2013 | Government systems · Workflow automation · Audit patterns · UI frameworks |
| 2013–2017 | Full-stack product delivery · Search engineering · E-Commerce · Payment integration · XML processing |
| 2017–2021 | Microservices · Event-driven architecture · Cloud migration · CI/CD · Platform modernisation |
| 2021–Present | Cloud-native architecture · AKS · Distributed systems · Async pipelines · Technical leadership · Mentoring |

---

## Key Career Milestones

| Year | Milestone |
|---|---|
| 2009 | First production code — ERP and CRM systems |
| 2011 | First government-grade system — Police Department BOM |
| 2013 | First end-to-end product ownership as Lead Developer |
| 2013 | First search engineering work — Elasticsearch geo-spatial directory |
| 2017 | First Technical Lead role — E-Marking Platform |
| 2018 | Led first microservices modernisation — Strangler Fig migration from WCF monolith |
| 2019 | Led first full DevOps transformation — IaC, CI/CD, blue/green, secrets management |
| 2020 | First offshore client go-live support — E-Marking Scanning Automation |
| 2021 | Solved critical production bottleneck — 91% reduction in marking pipeline start time |
| 2021 | Promoted to Senior Technical Lead (Architect) |
| 2022 | Designed compliance-grade archival system — AES-256, Key Vault, event-driven saga |
| Present | Associate Technical Architect — mentoring overseas implementation teams |

---

## Technologies Across the Career

```
Early Career          Mid Career              Current
─────────────         ──────────────────      ─────────────────────────
.NET Framework        Elasticsearch           .NET 6–8
ASP.NET WebForms      Google Maps API         ASP.NET Core
ADO.NET               RabbitMQ                AKS / Kubernetes
SQL Server            MassTransit             Azure Service Bus
jQuery                gRPC                    CosmosDB
Infragistics          Docker                  Azure Key Vault
XML / XSLT            React.js                KEDA
Bootstrap             Azure DevOps            ARM Templates / IaC
Payment Gateways      TeamCity                FFmpeg / LibreOffice
ASMX Web Services     Octopus Deploy          Chromium Headless
WCF                   Elsa Workflows          Razor RCL
Silverlight           Identity Server         Serilog + App Insights
```

---

*This timeline was prepared as part of the [project portfolio](./README.md).*