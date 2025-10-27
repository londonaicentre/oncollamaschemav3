## OncoLlama v3 Schema

This repo contains the pydantic schema that defines outputs for v3 of the OncoLlama cancer data extraction LLM.

### Field Naming Conventions

This schema follows consistent naming patterns for field suffixes:

#### Suffix Patterns

- `*_type` - Classification fields that map to enum values (e.g., topography_type, event_type)
- `*_status` - Fields that map to status enums (e.g., biomarker_status, msi_status)
- `*_name_desc` - Direct extraction of specific names/terms as they appear in clinical text (e.g., topography_name_desc, biomarker_name_desc)
- `*_desc` - Verbatim text extracts from source documents providing full context (e.g., event_desc, ps_desc, biomarker_desc)
- `*_summary` - Concise summaries of content (e.g., event_summary, patient_finding_summary)
- `*_value` - Value fields that may be string or numeric (e.g., score_value, ps_score_value)
- `*_numeric_value` - Explicitly numeric values only (e.g., tmb_numeric_value, biomarker_vaf_numeric_value)
- `*_year` and `*_month` - Temporal fields with validation constraints
- `*_flag` - Boolean indicator fields (e.g., document_has_primary_cancer_flag)

#### Other Principles

- Required enum fields have no defaults to ensure explicit classification
- Optional fields default to None to distinguish "not present" from "uncategorised" (OTHER)
- The `other_` prefix indicates secondary/historical cancer information distinct from primary cancer

### Example

```json
{
  "content": "Dear Dr. Harrison,\n\nI am writing to update you on Mrs. Margaret Thompson, a 68-year-old woman with metastatic lung adenocarcinoma, whom I reviewed in clinic today following her recent molecular profiling and disease reassessment.\n\nAs you know, Mrs. Thompson initially presented in March 2023 with a persistent cough and weight loss. CT imaging at that time revealed a 4.2cm right upper lobe mass with mediastinal lymphadenopathy. Bronchoscopy with EBUS-guided biopsy confirmed adenocarcinoma of the lung. Her initial staging was T2bN2M1b, stage IVA, with metastases identified in the liver and left adrenal gland. The pathological grading showed a poorly differentiated tumor, grade 3.\n\nComprehensive genomic profiling performed in April 2023 revealed several significant findings. Most notably, she harbors an EGFR exon 19 deletion with a variant allele frequency of 34%. Additionally, testing showed TP53 mutation p.R273H present at 28% VAF. Her tumor is PD-L1 positive with expression of 65% by immunohistochemistry. Testing for ALK rearrangement by FISH was negative. ROS1 testing was also negative. The tumor showed microsatellite stability (MSS) and a low tumor mutational burden of 3.2 mutations per megabase.\n\nMrs. Thompson commenced first-line treatment with osimertinib 80mg daily in May 2023, which she initially tolerated well with an excellent partial response on her August 2023 scan showing 45% reduction in tumor burden by RECIST criteria. Unfortunately, she developed a grade 2 acneiform rash in September 2023 requiring dose reduction to 40mg daily and treatment with topical clindamycin.\n\nIn February 2024, routine surveillance imaging demonstrated disease progression with new bilateral pulmonary nodules and enlargement of the liver metastases. She was considered for the KEYNOTE clinical trial but was ultimately deemed ineligible due to her performance status decline. Following multidisciplinary team discussion, she transitioned to carboplatin and pemetrexed chemotherapy in March 2024.\n\nRegrettably, Mrs. Thompson experienced significant treatment-related toxicity with grade 3 neutropenia after cycle 2, requiring hospital admission in April 2024 for febrile neutropenia. Treatment was subsequently stopped after 3 cycles due to poor tolerance and minimal response.\n\nDuring today's consultation, Mrs. Thompson appeared cachectic and reported losing a further 5kg over the past month, now weighing 52kg. She describes severe fatigue limiting her to bed or chair for more than 50% of waking hours, consistent with an ECOG performance status of 3. She reports moderate right-sided pleuritic chest pain, well-controlled with regular paracetamol and as-needed morphine sulfate. She denies any dyspnea at rest but becomes breathless with minimal exertion. Physical examination revealed reduced air entry at the right base with dullness to percussion, suggesting a pleural effusion. She appeared anxious about her prognosis and became tearful when discussing future planning.\n\nHer past medical history includes type 2 diabetes mellitus managed with metformin, and hypertension controlled with ramipril. She is a former smoker with a 30 pack-year history, having quit in 2020. She lives with her supportive husband and has good family support from her two adult children who live locally.\n\nMoving forward, we have arranged for a therapeutic pleurocentesis next week to address her symptomatic pleural effusion. We plan to obtain additional molecular profiling on the pleural fluid to assess for resistance mechanisms, particularly looking for MET amplification or EGFR T790M mutation. Given her current performance status, we are considering enrollment in a phase I trial of a novel EGFR/MET bispecific antibody if she meets eligibility criteria. Palliative radiotherapy to the right hemithorax is also being arranged to help with local symptom control.\n\nI have had a frank discussion with Mrs. Thompson and her husband about her prognosis and the transition toward a more palliative approach. We have initiated referral to the community palliative care team for additional support. She wishes to remain at home as long as possible and is not for cardiopulmonary resuscitation.\n\nI will continue to monitor her closely and keep you updated on any significant developments. Please do not hesitate to contact me if you require any additional information.\n\nYours sincerely,\n\nDr. Sarah Mitchell\nConsultant Medical Oncologist\nRegional Cancer Centre",
  "output": {
    "document_has_primary_cancer_flag": true,
    "primary_cancer_confirmed_flag": true,
    "primary_cancer": {
      "primary_cancer_facts": {
        "topography": "lung",
        "topography_name_desc": "right upper lobe",
        "morphology": "adenocarcinoma",
        "morphology_name_desc": "adenocarcinoma of the lung",
        "is_recurrence": false,
        "diagnosis_year": 2023,
        "diagnosis_month": 3,
        "tnm_stage": "T2bN2M1b",
        "numeric_group_stage": "IVA"
      },
      "primary_cancer_tumour_facts": {
        "msi_status": "mss",
        "msi_desc": "microsatellite stability (MSS)",
        "tmb_status": "tmb_low",
        "tmb_numeric_value": 3.2,
        "tmb_desc": "low tumor mutational burden of 3.2 mutations per megabase",
        "molecular_biomarker_profiles": [
          {
            "biomarker": "egfr",
            "biomarker_name_desc": "EGFR",
            "biomarker_status": "altered",
            "biomarker_alteration": "exon 19 deletion",
            "biomarker_expression_level": null,
            "biomarker_vaf_numeric_value": 34.0,
            "biomarker_vaf_desc": "variant allele frequency of 34%",
            "biomarker_desc": "EGFR exon 19 deletion with a variant allele frequency of 34%"
          },
          {
            "biomarker": "tp53",
            "biomarker_name_desc": "TP53",
            "biomarker_status": "altered",
            "biomarker_alteration": "p.R273H",
            "biomarker_expression_level": null,
            "biomarker_vaf_numeric_value": 28.0,
            "biomarker_vaf_desc": "28% VAF",
            "biomarker_desc": "TP53 mutation p.R273H present at 28% VAF"
          },
          {
            "biomarker": "pdl1",
            "biomarker_name_desc": "PD-L1",
            "biomarker_status": "altered",
            "biomarker_alteration": null,
            "biomarker_expression_level": "65%",
            "biomarker_vaf_numeric_value": null,
            "biomarker_vaf_desc": null,
            "biomarker_desc": "PD-L1 positive with expression of 65% by immunohistochemistry"
          },
          {
            "biomarker": "alk",
            "biomarker_name_desc": "ALK",
            "biomarker_status": "negative",
            "biomarker_alteration": null,
            "biomarker_expression_level": null,
            "biomarker_vaf_numeric_value": null,
            "biomarker_vaf_desc": null,
            "biomarker_desc": "ALK rearrangement by FISH was negative"
          },
          {
            "biomarker": "ros1",
            "biomarker_name_desc": "ROS1",
            "biomarker_status": "negative",
            "biomarker_alteration": null,
            "biomarker_expression_level": null,
            "biomarker_vaf_numeric_value": null,
            "biomarker_vaf_desc": null,
            "biomarker_desc": "ROS1 testing was also negative"
          },
          {
            "biomarker": "met",
            "biomarker_name_desc": "MET",
            "biomarker_status": "hypothetical",
            "biomarker_alteration": "amplification",
            "biomarker_expression_level": null,
            "biomarker_vaf_numeric_value": null,
            "biomarker_vaf_desc": null,
            "biomarker_desc": "looking for MET amplification"
          }
        ]
      },
      "primary_cancer_scores": [
        {
          "score": "pathological_grade",
          "score_name_desc": "pathological grading",
          "score_value": "3",
          "score_value_desc": "grade 3"
        }
      ],
      "primary_cancer_spread": [
        {
          "spread_type": "liver",
          "spread_site_desc": "liver"
        },
        {
          "spread_type": "adrenal",
          "spread_site_desc": "left adrenal gland"
        },
        {
          "spread_type": "lung",
          "spread_site_desc": "bilateral pulmonary nodules"
        },
        {
          "spread_type": "pleura",
          "spread_site_desc": "pleural effusion"
        }
      ],
      "primary_cancer_timeline_events": [
        {
          "event_type": "had_systemic_or_radiotherapy_treatment",
          "event_year": 2023,
          "event_month": 5,
          "event_summary": "Started first-line osimertinib 80mg daily",
          "event_desc": "commenced first-line treatment with osimertinib 80mg daily in May 2023"
        },
        {
          "event_type": "positive_treatment_response_on_assessment",
          "event_year": 2023,
          "event_month": 8,
          "event_summary": "Excellent partial response with 45% tumor reduction",
          "event_desc": "excellent partial response on her August 2023 scan showing 45% reduction in tumor burden by RECIST criteria"
        },
        {
          "event_type": "experienced_toxicity_or_complication_related_to_treatment",
          "event_year": 2023,
          "event_month": 9,
          "event_summary": "Grade 2 acneiform rash requiring dose reduction",
          "event_desc": "developed a grade 2 acneiform rash in September 2023 requiring dose reduction to 40mg daily"
        },
        {
          "event_type": "radiology_evidence_of_disease_progression",
          "event_year": 2024,
          "event_month": 2,
          "event_summary": "Disease progression with new lung nodules and liver metastases growth",
          "event_desc": "routine surveillance imaging demonstrated disease progression with new bilateral pulmonary nodules and enlargement of the liver metastases"
        },
        {
          "event_type": "considered_for_clinical_trial",
          "event_year": 2024,
          "event_month": 2,
          "event_summary": "Considered but ineligible for KEYNOTE trial",
          "event_desc": "considered for the KEYNOTE clinical trial but was ultimately deemed ineligible due to her performance status decline"
        },
        {
          "event_type": "experienced_treatment_reduction_or_stop",
          "event_year": 2024,
          "event_month": 4,
          "event_summary": "Chemotherapy stopped after 3 cycles due to poor tolerance",
          "event_desc": "Treatment was subsequently stopped after 3 cycles due to poor tolerance and minimal response"
        }
      ]
    },
    "performance_status": {
      "ps_scale": "ECOG",
      "ps_score_value": "3",
      "ps_desc": "severe fatigue limiting her to bed or chair for more than 50% of waking hours, consistent with an ECOG performance status of 3"
    },
    "other_cancers": null,
    "patient_findings": [
      {
        "patient_finding_type": "symptom_finding",
        "patient_finding_name_desc": "Lost 5kg in past month, now 52kg",
        "patient_finding_desc": "losing a further 5kg over the past month, now weighing 52kg",
        "patient_finding_status": "is_present"
      },
      {
        "patient_finding_type": "physical_examination_finding",
        "patient_finding_name_desc": "Cachectic appearance",
        "patient_finding_desc": "Mrs. Thompson appeared cachectic",
        "patient_finding_status": "is_present"
      },
      {
        "patient_finding_type": "symptom_finding",
        "patient_finding_name_desc": "Moderate right-sided pleuritic chest pain",
        "patient_finding_desc": "moderate right-sided pleuritic chest pain, well-controlled with regular paracetamol and as-needed morphine sulfate",
        "patient_finding_status": "is_present"
      },
      {
        "patient_finding_type": "symptom_finding",
        "patient_finding_name_desc": "No dyspnea at rest but breathless on minimal exertion",
        "patient_finding_desc": "denies any dyspnea at rest but becomes breathless with minimal exertion",
        "patient_finding_status": "is_present"
      },
      {
        "patient_finding_type": "comorbidity_finding",
        "patient_finding_name_desc": "Type 2 diabetes on metformin",
        "patient_finding_desc": "type 2 diabetes mellitus managed with metformin",
        "patient_finding_status": "is_present"
      },
      {
        "patient_finding_type": "mental_state_finding",
        "patient_finding_name_desc": "Anxious and tearful about prognosis",
        "patient_finding_desc": "appeared anxious about her prognosis and became tearful when discussing future planning",
        "patient_finding_status": "is_present"
      }
    ],
    "future_plans": [
      {
        "future_plan_type": "planned_investigation",
        "future_plan_summary": "Therapeutic pleurocentesis next week",
        "future_plan_desc": "arranged for a therapeutic pleurocentesis next week to address her symptomatic pleural effusion"
      },
      {
        "future_plan_type": "planned_investigation",
        "future_plan_summary": "Molecular profiling on pleural fluid for resistance mechanisms",
        "future_plan_desc": "obtain additional molecular profiling on the pleural fluid to assess for resistance mechanisms, particularly looking for MET amplification or EGFR T790M mutation"
      },
      {
        "future_plan_type": "planned_clinical_trial_involvement",
        "future_plan_summary": "Possible phase I trial of EGFR/MET bispecific antibody",
        "future_plan_desc": "considering enrollment in a phase I trial of a novel EGFR/MET bispecific antibody if she meets eligibility criteria"
      },
      {
        "future_plan_type": "planned_systemic_or_radiotherapy_treatment",
        "future_plan_summary": "Palliative radiotherapy to right hemithorax",
        "future_plan_desc": "Palliative radiotherapy to the right hemithorax is also being arranged to help with local symptom control"
      }
    ],
    "context_summary": {
      "doc_context": "Oncology clinic letter",
      "doc_summary": "Patient with advanced lung adenocarcinoma experiencing disease progression after initial EGFR-targeted therapy and subsequent chemotherapy, now transitioning to palliative care with poor performance status"
    }
  }
}
```