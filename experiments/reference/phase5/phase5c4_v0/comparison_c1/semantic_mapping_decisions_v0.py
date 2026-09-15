"""Private comparison judgments, never final gold or correctness decisions.

Keys are 1-based positions in the hash-bound A source, not candidate matches.
Candidate alignment is exclusively the verified canonical/B-local mapping.
Aspect positions are zero-based. All source aspects must occur exactly once.
These decisions follow direct reading of both propositions and bounded scopes;
they are not a text-similarity threshold or evidence-ID-only match.
"""

def g(a, b, relation='equivalent', reason='Same bounded proposition and legal role; wording differs.', boundary=False):
    return {'A': a if isinstance(a, list) else [a], 'B': b if isinstance(b, list) else [b],
            'relation': relation, 'reason': reason, 'additional_boundary_difference': boundary}

DECISIONS = {
1: [g(0,1),g(1,0),g(2,[], 'A_only','Human control/responsibility is a distinct A aspect.'),g([],2,'B_only','Display-label exception is a distinct B aspect.'),g([],3,'B_only','Safety and incident prevention is a distinct B aspect.')],
2: [g(0,0),g(1,1),g(2,2,'B_broader','B adds publication of assessment results.'),g(3,3,'B_broader','B adds deployer operation, monitoring and intervention to handover.'),g([],4,'B_only','Classification notification and allocation of further responsibilities appear only as a B required aspect.')],
3: [g(0,3),g(1,1,'B_broader','B additionally requires maintaining/publicizing conformity.'),g(2,0,'B_broader','B additionally includes preparation of classification documentation.'),g(3,4,'B_broader','B combines interaction notice with limits and incident coordination.'),g([],2,'B_only','Risk/data/control/handover duties are independently required by B.')],
4: [g(0,[0,1],'A_split_into_B','A combines voluntary participation with unchanged ownership; B separates them.'),g(1,2),g(2,3,'ambiguous','Security/access overlap, but A specifies secrecy and B adds technical connection requirements.',True),g(3,[],'A_only','Infrastructure energy/emissions obligations are an A-only aspect.')],
5: [g(0,0),g(1,1,'B_broader','B combines publication with substantive impact-report contents.'),g(2,3,'B_broader','B adds privacy/equality assessment to bias and vulnerable-group assessment.'),g(3,2),g([],4,'B_only','Transparency, complaints and accountability add a B required aspect.')],
6: [g(0,[0,1],'A_split_into_B','Label trigger and placement are separated by B; B also explicitly mentions misleading-content notification.',True),g(1,2,'B_broader','B adds voluntary-framework scope and transparency limits to the cultural aspect.'),g(2,3)],
7: [g(0,0),g(1,1),g([2,3],3,'ambiguous','A distinguishes provider marking-function maintenance and non-removal; B broadly assigns transparency preservation to both parties.',True),g([],2,'B_only','Conditional visible labeling/notice is distinct from machine-readable marking.')],
8: [g(0,0),g(1,3),g([2,3],2,'B_split_into_A','B combines records/logs with maintained conformity and updated published results; A additionally states proportionality/secrecy.',True),g([],1,'B_only','B separately requires updating risk/data/human-control management.'),g([],4,'B_only','Conditional reclassification is separately required by B.')],
9: [g(0,0),g(1,1),g(2,2),g([],3,'B_only','Inclusive access and digital-divide duties add a B aspect.')],
10: [g(0,0),g(1,2),g(2,3,'B_broader','B combines complaint/remediation channels with express allocation of accountability.'),g([],1,'B_only','B independently adds bias/vulnerable-group assessment.')],
11: [g(0,[0,1],'A_split_into_B','A combines transition duration and authority to suspend; B separates them.'),g(1,2),g(2,3),g(3,[],'A_only','Framework applicability/effective date is required only as an A aspect.')],
12: [g(0,0),g(1,1,'B_broader','B adds third-party interference and possible joint liability to exemptions.'),g(2,3),g([],2,'B_only','B separately requires preventive monitoring/intervention.'),g([],4,'B_only','B adds optional insurance/security arrangements.')],
13: [g([0,1],[0,1,2],'ambiguous','Access limits and user obligations overlap across two A and three B aspects; B2 partly repeats B0/B1 rather than an independently matched duty.',True),g(2,3)],
14: [g(0,3,'B_broader','B adds cultural/non-discrimination concerns to open research/IP.'),g(1,0),g(2,1),g([],2,'B_only','B adds voluntary information submission.'),g([],4,'B_only','B adds transparency and complaint/responsibility arrangements.')],
15: [g(0,0,'equivalent','Both apply the exclusive-defence exception to the same bounded activity; A names additional exception categories without changing that conclusion.')],
16: [g(0,0,'B_broader','B adds prohibition on additional application components.'),g(1,[1,2],'A_split_into_B','B separates submission/authority from processing period and adds reasons for refusal.',True),g(2,3)],
17: [g(0,0),g([1,2],[1,2,3],'ambiguous','Documentation, service reconciliation, direct payment and non-cash/non-transfer rules cross aspect boundaries on both sides; B also adds voucher conditions.',True)],
18: [g(0,0),g(1,1,'B_broader','B includes report form and substantive contents alongside approval/accountability.'),g(2,3,'B_broader','B adds cooperation/learning to staff training.'),g([],2,'B_only','Publication and retained human decision responsibility are additional B requirements.')],
19: [g(0,0),g(1,1),g(2,2,'A_broader','A includes authority determination and electronic notice of support level/conditions; B limits the aspect to use and reporting obligations.')],
20: [g(0,0),g(1,2,'B_broader','B adds maintained conformity and updates following reassessment.'),g(2,3),g([],1,'B_only','B independently includes conditional assessment-route selection.')],
21: [g(0,0),g(1,1),g(2,2)],
22: [g(0,0),g(1,1),g(2,2)],
23: [g(0,0),g(1,1),g(2,2),g(3,3,'B_broader','B adds confidentiality/integrity/availability and incident response to re-identification/model attacks.')],
24: [g([0,1,2],[0,1],'ambiguous','Provider role, lawful access limits, secrecy and equivalent documentation are repartitioned across aspect boundaries; B additionally requires a classification dossier.',True),g(3,2)],
25: [g(0,1),g(1,[0,2],'A_split_into_B','B separates mandatory trigger from label placement.'),g(2,[],'A_only','Ongoing transparency preservation and non-removal are not a separate B aspect.')],
26: [g(0,0),g(1,1,'B_broader','B adds prohibition on additional dossier components.'),g(2,3,'A_broader','A additionally covers trade promotion and major programs; B bounds the benefit aspect to infrastructure/training.'),g(3,2)],
27: [g(0,0,'A_broader','A explicitly includes notification before use; B proposition emphasizes electronic route and dossier contents.'),g(1,1),g(2,2,'B_broader','B additionally states provider responsibility for declared contents.')],
28: [g(0,0),g([1,2],[1,2],'ambiguous','API/environment, ownership and access/user controls are cross-partitioned; B focuses API and A also names secure on-premise environment.',True)],
29: [g(0,[0,1],'A_split_into_B','B separates submission/deadlines from extension eligibility; applicability differs on the eligibility component.'),g([1,2],2,'B_split_into_A','B combines completed compliance after transition with non-substitution of sectoral permissions.')],
30: [g(0,0),g(1,1)],
31: [g(0,0)],32: [g(0,0)],33: [g(0,0)],34: [g(0,0)],35: [g(0,0)],
36: [g(0,0,'A_broader','A separately conditions technical developer status on control of methods/data/parameters; B focuses the brand-owning provider conclusion.')],
37: [g(0,0)],38: [g(0,0),g(1,1)],
39: [g(0,0),g(1,[],'A_only','A independently requires discrimination of sandbox financial-security conditions; B keeps only the outside-sandbox insurance proposition.')],
40: [g(0,0,'B_broader','B additionally specifies confidentiality, integrity and availability alongside poisoning prevention.')],
41: [g(0,[0,1],'A_split_into_B','B separates rejection of level-2 inference from level-1 conclusion and adds competent-authority determination.',True)],
42: [g(0,0),g(1,1)],43: [g(0,0)],
44: [g(0,0,'B_broader','B expressly covers voluntary provision of information as well as optional form use.')],
45: [g([0,1],0,'B_split_into_A','B combines the supported baseline contact duty and unresolved certification-condition qualification; A scores those separately.')],
46: [g(0,0),g(1,1)],47: [g(0,0),g(1,1)],48: [g(0,0)],49: [g(0,0)],50: [g(0,0),g(1,1)],
51: [g(0,[0,2],'A_split_into_B','A keeps storage duty and absent post-cessation duration in one partial aspect; B separates supported duty from absent duration and adds classification-file retention.',True),g(1,1)],
52: [g(0,0),g(1,1),g(2,2)],53: [g(0,0),g(1,1)],54: [g(0,0)],55: [g(0,0)],56: [g(0,0)],57: [g(0,0)],58: [g(0,0),g(1,1)],59: [g(0,0)],
60: [g(0,0,'ambiguous','Both leave the requested start date unresolved, but A treats the whole requested proposition as absent while B credits a partially supported transition rule; support/credit boundary remains unresolved.',True)]
}

SCOPE_MATERIAL_PAIRS = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,18,19,20,24,25,26,27,28,36,39,40,44,51,60}
ACTOR_REVIEW_PAIRS = {2,7,24,36}
CONDITION_REVIEW_PAIRS = {7,8,11,12,20,29,36,45,60}
