import json, re

HUB_URL = "https://www.sixthcitymarketing.com/local-seo/"
BASE = "https://www.sixthcitymarketing.com"

def eid(url):
    path = url.replace(BASE, "").strip("/")
    slug = re.sub(r"[^a-z0-9]+", "_", path.lower()).strip("_")
    return "p_" + (slug or "home")

# (name, url, predicate, type, needs_confidence)
targets = [
    # --- sibling services (RELATES_TO / PART_OF) ---
    ("SEO & AI Search Services", f"{BASE}/services/search-engine-optimization/", "PART_OF", "Service", False),
    ("Link Building", f"{BASE}/link-building-services/", "RELATES_TO", "Service", False),
    ("Conversion Rate Optimization", f"{BASE}/services/conversion-rate-optimization/", "RELATES_TO", "Service", False),
    ("Pay-Per-Click", f"{BASE}/services/pay-per-click/", "RELATES_TO", "Service", False),
    ("Paid Social Media Ads", f"{BASE}/services/paid-social-media/", "RELATES_TO", "Service", False),
    ("Website Design", f"{BASE}/services/design/", "RELATES_TO", "Service", False),
    ("Social Media Marketing", f"{BASE}/services/social-media-marketing/", "RELATES_TO", "Service", False),
    ("Consulting & Auditing", f"{BASE}/services/consulting-auditing/", "RELATES_TO", "Service", False),

    # --- industries served (SUITED_FOR, confidence required) ---
    ("Dental Practices", f"{BASE}/dental-seo-agency/", "SUITED_FOR", "Service", True),
    ("Legal Practices", f"{BASE}/legal-seo/", "SUITED_FOR", "Service", True),
    ("Senior Care", f"{BASE}/senior-living-seo/", "SUITED_FOR", "Service", True),
    ("Car Dealerships", f"{BASE}/automotive-seo/", "SUITED_FOR", "Service", True),
    ("Retail / Ecommerce", f"{BASE}/ecommerce-seo/", "SUITED_FOR", "Service", True),
    ("Psychologists / Therapists", f"{BASE}/therapist-seo/", "SUITED_FOR", "Service", True),
    ("Medical / Healthcare", f"{BASE}/healthcare-seo/", "SUITED_FOR", "Service", True),
    ("Finance Offices", f"{BASE}/financial-seo/", "SUITED_FOR", "Service", True),
    ("Franchises", f"{BASE}/franchise-seo/", "SUITED_FOR", "Service", True),
    ("Architects / Engineers", f"{BASE}/aec-marketing-seo/", "SUITED_FOR", "Service", True),
    ("Cannabis Retailers", f"{BASE}/cannabis-seo/", "SUITED_FOR", "Service", True),
    ("Home Services", f"{BASE}/home-services-seo/", "SUITED_FOR", "Service", True),
    ("Plumbers", f"{BASE}/plumber-seo/", "SUITED_FOR", "Service", True),
    ("Contractors", f"{BASE}/contractor-seo/", "SUITED_FOR", "Service", True),
    ("Roofers", f"{BASE}/roofing-seo/", "SUITED_FOR", "Service", True),
    ("Painters", f"{BASE}/seo-for-painting-companies/", "SUITED_FOR", "Service", True),
    ("Construction", f"{BASE}/construction-seo/", "SUITED_FOR", "Service", True),
    ("HVAC", f"{BASE}/hvac-seo/", "SUITED_FOR", "Service", True),
    ("Garage Door Installers", f"{BASE}/garage-door-seo/", "SUITED_FOR", "Service", True),
    ("Fence Installers", f"{BASE}/fencing-company-seo/", "SUITED_FOR", "Service", True),
    ("Landscapers", f"{BASE}/landscaping-seo/", "SUITED_FOR", "Service", True),
    ("Electricians", f"{BASE}/electrician-seo/", "SUITED_FOR", "Service", True),
    ("Cleaning Companies", f"{BASE}/industries/commercial-cleaners/", "SUITED_FOR", "Service", True),
    ("Remodelers / Home Builders", f"{BASE}/home-builder-seo/", "SUITED_FOR", "Service", True),
    ("Waste / Recycling", f"{BASE}/waste-management-seo/", "SUITED_FOR", "Service", True),
    ("Snow Plow Companies", f"{BASE}/seo-for-snow-plows/", "SUITED_FOR", "Service", True),
    ("Pest Control", f"{BASE}/pest-control-seo/", "SUITED_FOR", "Service", True),
    ("Window Companies", f"{BASE}/seo-for-window-companies/", "SUITED_FOR", "Service", True),
    ("Veterinarians", f"{BASE}/2024/09/27/seo-for-veterinarians/", "SUITED_FOR", "Service", True),
    ("ABA Therapists", f"{BASE}/2025/07/02/aba-therapy-marketing/", "SUITED_FOR", "Service", True),
    ("Trade Schools", f"{BASE}/2024/10/04/seo-for-trade-schools/", "SUITED_FOR", "Service", True),

    # --- locations covered (COVERS, Place) ---
    ("Cleveland", f"{BASE}/search-engine-optimization-cleveland/", "COVERS", "Place", False),
    ("Columbus", f"{BASE}/columbus-seo/", "COVERS", "Place", False),
    ("Pittsburgh", f"{BASE}/pittsburgh-seo/", "COVERS", "Place", False),
    ("Indianapolis", f"{BASE}/indianapolis-seo-services/", "COVERS", "Place", False),
    ("Chicago", f"{BASE}/chicago-seo/", "COVERS", "Place", False),
    ("Nashville", f"{BASE}/nashville-seo/", "COVERS", "Place", False),

    # --- resources / proof / conversion (RELATES_TO) ---
    ("Types of SEO (guide)", f"{BASE}/2024/05/20/types-of-seo/", "RELATES_TO", "Concept", False),
    ("Social Media Statistics", f"{BASE}/social-media-stats/", "RELATES_TO", "Concept", False),
    ("Case Studies", f"{BASE}/about-sixth-city-marketing/case-studies/", "DESCRIBED_BY", "Concept", False),
    ("Contact / Lead Form", f"{BASE}/contact/", "RELATES_TO", "Concept", False),
]

def chunk(name, url):
    return [{
        "chunkId": "c_" + eid(url),
        "text": f"{name} is an internal page on sixthcitymarketing.com linked contextually from the Local SEO service page.",
        "sourceUrl": url,
        "pageTitle": name,
        "publisher": "Sixth City Marketing"
    }]

hub = {
    "entityId": "p_local_seo",
    "@type": "Service",
    "name": "Local SEO Services",
    "description": "Sixth City Marketing's Local SEO service page. This node is the hub; edges represent the contextual (in-body) internal links found on the page, grouped by purpose: COVERS = city pages, SUITED_FOR = industries served, RELATES_TO/PART_OF = sibling services and resources.",
    "relations": [],
    "hasChunks": [{
        "chunkId": "c_p_local_seo",
        "text": "Local SEO helps your business appear in location-based and map searches so nearby customers can find you.",
        "sourceUrl": HUB_URL,
        "pageTitle": "Local SEO Services To Help You Rank in the Local Pack",
        "publisher": "Sixth City Marketing"
    }]
}

entities = [hub]
for name, url, pred, typ, conf in targets:
    rel = {"predicate": pred, "targetId": eid(url), "targetName": name}
    if conf:
        rel["confidence"] = "declared"
    hub["relations"].append(rel)
    entities.append({
        "entityId": eid(url),
        "@type": typ,
        "name": name,
        "description": f"Internal page: {name} ({url}).",
        "hasChunks": chunk(name, url)
    })

doc = {
    "version": "1.0",
    "schema": "https://entitymap.org/spec/v1.0",
    "generated": "2026-06-05T00:00:00Z",
    "verificationStatus": "self-declared",
    "publisher": {"name": "Sixth City Marketing", "url": "https://www.sixthcitymarketing.com/"},
    "entities": entities
}

out = "/Users/briangormanh/briangormanh.com/Claude Code/entitymap-pages/local-seo-linkmap.json"
with open(out, "w") as f:
    json.dump(doc, f, indent=2)
print(f"{len(entities)} nodes, {len(hub['relations'])} edges written to local-seo-linkmap.json")
