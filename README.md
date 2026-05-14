# Anoop Nadakkara Palliyan — Project Portfolio

**Associate Technical Architect · Senior .NET Consultant · Senior Technical Lead**

15+ years of IT experience specialising in scalable SaaS-based web applications, cloud-native microservices architecture, and enterprise platform modernisation on the Microsoft technology stack. This portfolio presents case studies across all major projects — covering architecture decisions, technical implementations, challenges solved, and measurable outcomes.

---

## Core Competencies

| Area | Skills |
|---|---|
| **Languages** | C#, VB.NET, ASP.NET, T-SQL, JavaScript, TypeScript |
| **Frameworks** | .NET Core, .NET 5–8, ASP.NET MVC, Web API, Entity Framework, EF Core, Blazor, SignalR |
| **Architecture** | Microservices, DDD, SOA, SOLID, Clean Architecture, Event-Driven Architecture |
| **Cloud & DevOps** | Azure App Services, AKS, Cosmos DB, Key Vault, CI/CD via Azure DevOps, Docker, Kubernetes |
| **Messaging** | RabbitMQ, MassTransit, Azure Service Bus |
| **Databases** | SQL Server, Cosmos DB, MongoDB, Elasticsearch |
| **Frontend** | React.js, Razor Components, jQuery, Blazor |

---

## Case Studies

### Architect & Technical Lead Role

Projects where architectural ownership, system design, and technical leadership were the primary responsibility.

---

#### 1. Engagement Retention & Archiving Solution
> **Senior Technical Lead (Architect)** · .NET 6 · Microservices · AKS · Azure Service Bus · CosmosDB · AES Encryption

Compliance-driven archival subsystem preserving completed audit engagements in portable, encrypted, cloud-stored packages with on-demand reproduction capability. Decoupled historical data from live systems via an event-driven async pipeline with per-package AES-256 encryption and Azure Key Vault key management.

[→ View Case Study](./case-studies/1.%20engagement-archiving-solution.md)

---

#### 2. Digital E-Marking Scanning Automation
> **Technical Lead** · .NET 5 · RabbitMQ · MassTransit · gRPC · Elsa Workflows · AKS · Scantron SDK

Distributed microservices extension enabling universities to automate high-volume exam response scanning across OMR, descriptive, and hybrid response types. Configurable Elsa Workflow pipelines per exam type with async event-driven ingestion via RabbitMQ and MassTransit.

[→ View Case Study](./case-studies/2.%20digital-e-marking-scanning-automation.md)

---

#### 3. Digital E-Marking Assessment Platform
> **Technical Lead** · .NET · Microservices · RabbitMQ · gRPC · React.js · AKS · Strangler Fig Migration

Enterprise-grade digital assessment platform modernised from a WCF/Silverlight monolith to cloud-native microservices with a React.js frontend. Incremental Strangler Fig migration with zero downtime, database-per-service decomposition, and new modules for marker management, SLA tracking, and statistical analytics.

[→ View Case Study](./case-studies/3.%20digital-e-marking-assessment-platform.md)

---

#### 3b. Document Conversion Service *(Deep Dive)*
> **Technical Lead** · .NET · FFmpeg · LibreOffice Headless · Ghostscript · Chromium Headless · RabbitMQ · AKS · KEDA

High-throughput multimedia conversion engine supporting scanned images, audio, video, Office documents, PDFs, and HTML files. Parallel format-specific worker pools with KEDA queue-depth autoscaling eliminated a critical marking pipeline bottleneck — reducing time to first marker availability from ~45 minutes to ~4 minutes on a 5,000-file batch.

[→ View Case Study](./case-studies/4.%20digital-e-marking-document-conversion-service.md)

---

#### 4. Digital E-Marking Platform — Cloud Migration & DevOps Transformation
> **Technical Lead** · Azure DevOps · TeamCity · Octopus Deploy · ARM Templates · AKS · Docker · IaC

End-to-end DevOps transformation — CI/CD pipeline design, Infrastructure as Code with ARM templates, blue/green deployment with automated rollback, and full secrets migration to Azure Key Vault. Reduced time from merge to production from hours of manual coordination to under 30 minutes.

[→ View Case Study](./case-studies/5.%20digital-e-marking-cloud-devops-migration.md)

---

#### 5. Digital E-Marking Platform — Administration Interface
> **Technical Lead** · ASP.NET MVC · C# · .NET Framework · jQuery · ASMX · SQL Server · Infragistics

Centralised administration interface for the digital marking ecosystem. Key delivery: the Zoning Module — enabling exam coordinators to split candidate scripts into independently assigned answer zones for specialist marker pools, with an interactive jQuery canvas tool for zone definition.

[→ View Case Study](./case-studies/6.%20digital-e-marking-admin-interface.md)

---

#### 6. Custom Social Networking — Bible Study Platform
> **Lead Developer** · ASP.NET MVC · C# · jQuery · XML · XSLT · Social Sign-In Integration

Custom social networking platform combining a full Bible reader with community features. Built an XML content processing pipeline supporting OSIS, ThML, and USX Bible standards with XSLT transformations and extended OSIS specification for platform-specific content elements. Verse-level social interaction (likes, bookmarks, comments, sharing) anchored to a canonical VerseRef model.

[→ View Case Study](./case-studies/7.%20custom-social-networking-bible-study.platform.md.md)

---

### Developer Role

Projects delivered as Lead Developer or Software Engineer — focused on feature ownership, full-stack implementation, and technical problem solving.

---

#### 7. Business Process Automation — Wood Veneer Processing Factory
> **Lead Developer** · ASP.NET MVC · C# · jQuery · SQL Server · Secure Image Storage

Digitised manual factory operations for a wood veneer manufacturer — stock management, conversion tracking, pattern photo documentation, and a client-facing showcase portal. Per-sheet veneer traceability from raw log intake through to sale via photo documentation and yield analytics.

[→ View Case Study](./projects/business-process-automation-wood-veneer-processing-fatory.md)

---

#### 8. Business Process Automation — Donation Management System
> **Lead Developer** · ASP.NET MVC · C# · jQuery · SQL Server · Custom Theming

Multi-tenant fundraising platform enabling organisations to create campaigns, engage donors, and track progress. Real-time campaign progress calculation, donation velocity projection, donor deduplication, and per-organisation branded instances without code deployments.

[→ View Case Study](./projects/business-process-automation-donation-management-system.md)

---

#### 9. E-Commerce Platform — Ayurvedic Cosmetics & Medicines
> **Lead Developer** · ASP.NET MVC · C# · jQuery · AJAX · SQL Server · Payment Gateway

Full-stack e-commerce platform purpose-built for Ayurvedic retail — ingredient transparency, regulatory disclaimer acknowledgement, product variant matrix, AJAX cart, and idempotent payment webhook handling.

[→ View Case Study](./projects/e-commerce-platform-ayurvedic-cosmetics-and-medicines.md)

---

#### 10. E-Commerce Platform — Health & Wellness Products
> **Lead Developer** · ASP.NET MVC · C# · jQuery · AJAX · SQL Server · Payment Gateway

Full-stack e-commerce platform with a promotional engine supporting percentage discounts, fixed-amount discounts, bundle offers, and discount codes. Optimistic concurrency on discount code redemption, back-in-stock notification, and promotion performance reporting.

[→ View Case Study](./projects/e-commerce-platform-health-and-welness-products.md)

---

#### 11. Business Directory Platform
> **Lead Developer** · ASP.NET MVC · C# · Elasticsearch · Google Maps API · SQL Server · jQuery

Location-aware business directory with Elasticsearch geo-distance search, Google Maps viewport-bounded discovery, and a subscription-based premium placement model implemented as a configurable function-score boost in the Elasticsearch query pipeline.

[→ View Case Study](./projects/business-directroy-platform.md)

---

#### 12. Coupons Directory & Promotion Platform
> **Lead Developer** · ASP.NET MVC · C# · Elasticsearch · Google Maps API · SQL Server · jQuery

Coupon discovery platform with location-aware search, subscription-tier placement boost, coupon lifecycle state machine, optimistic concurrency on redemption limit enforcement, and daily stat aggregation for campaign performance analytics.

[→ View Case Study](./projects/coupons-directory-and-promotion-platform.md)

---

#### 13. Back Office Management System — Police Department
> **Senior Software Engineer** · ASP.NET · C# · SQL Server · jQuery · Infragistics

Government back-office system for crew management, financial aid administration, and operational activity tracking. Configuration-driven approval chain routing, field-level audit trail interceptor, and SQL Server full-text search across the activity log.

[→ View Case Study](./projects/back-office-magement-system-police-department.md)

---

#### 14. Back Office Management System — ERP Stores
> **Software Engineer** · .NET · Web API · RabbitMQ · gRPC · Azure · SQL Server

Large-scale retail ERP enhancement including POS terminal integration via Web API and RabbitMQ for real-time billing and inventory sync. gRPC product master data push to POS terminals, offline resilience with local cache and idempotent transaction replay, and inventory event log as an immutable source of truth.

[→ View Case Study](./projects/back-office-management-system-erp-store.md)

---

#### 15. Web CRM System
> **Software Engineer** · ASP.NET · C# · SQL Server · jQuery · AJAX

Web-based CRM covering lead management, opportunity pipeline, activity logging, and ERP-integrated sales order generation. Lead duplicate detection with fuzzy phone matching, probability-weighted revenue forecasting, and unified activity timeline aggregation.

[→ View Case Study](./projects/web-crm-system.md)

---

## Architecture Patterns Across Projects

| Pattern | Projects |
|---|---|
| Event-Driven Architecture | 1, 2, 3, 3b, 14 |
| Microservices & DDD | 1, 2, 3, 3b, 4 |
| Saga (Choreography) | 1, 2, 3 |
| Strangler Fig Migration | 3, 4 |
| CQRS | 3, 3b |
| Infrastructure as Code | 4 |
| CI/CD Pipeline as Code | 4 |
| Horizontal Autoscaling (KEDA) | 3b |
| Elasticsearch Geo-Spatial Search | 11, 12 |
| State Machine | 8, 9, 10, 12, 15 |
| Optimistic Concurrency | 10, 12, 14 |
| Idempotent Consumer | 9, 14 |
| XML Pipeline & XSLT | 6 |
| Multi-Tenancy | 8 |
| Audit Interceptor | 13 |

---

## Contact

- **LinkedIn:** *(add your LinkedIn URL)*
- **Email:** *(add your email)*
- **Location:** Kerala, India