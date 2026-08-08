# E2-01-04 Hardware Lab Access

## Purpose

Complete Control & Mechatronics Lab user registration, safety training, and risk assessment before applying to enter the `E2-01-04` hardware laboratory for physical robot experiments.

!!! note "Separate location and application"
    This page applies only to `E2-01-04`. For `COM2-0106`, see the [laboratory access application](lab-access.en.md).

## Prerequisites

- Have an account that can sign in to NUS Canvas; NUS staff also need access to CHRS LMS.
- Review the project activities, equipment, and risk controls with your supervisor or laboratory staff.
- Prepare a personal photo for the registration submission.
- Use an office application that can edit the forms and export completed copies to PDF.

## Required Safety Training

| Course | Title | Platform | Audience |
| --- | --- | --- | --- |
| `OSHGEN01` | Laboratory Safety Induction Training | [NUS Canvas](https://www.nus.edu.sg/canvas/login/) (search under All Courses) | All laboratory users |
| `OSHGEN02` | Introduction to Laboratory Safety & Health in NUS | [NUS Canvas](https://www.nus.edu.sg/canvas/login/) (search under All Courses) | All laboratory users |
| `OSHGEN03` | NUS Requirements on Safety, Health & Emergency Management | CHRS LMS | Staff only |
| `OSHGEN06` | Risk Management for Laboratory | [NUS Canvas](https://www.nus.edu.sg/canvas/login/) (search under All Courses) | All laboratory users |
| `OSHERGO02` | NUS Laboratory Ergonomics Training | [NUS Canvas](https://www.nus.edu.sg/canvas/login/) (search under All Courses) | All laboratory users |
| `OSHFS01` | Online Fire Safety Training Course | CHRS LMS | Staff only |

Supplementary material for `OSHGEN06` includes *Risk Management for Workplace* and [Risk Assessment Overview (Dept of ME)](https://mediaweb.ap.panopto.com/Panopto/Pages/Viewer.aspx?id=e3086fa8-8e25-474e-a580-aa07008152cb).

## Application Procedure

1. Complete the safety training applicable to your role and record each completion date.
2. Complete the user registration form and risk assessment form; review the risk assessment with your supervisor or laboratory staff.
3. Export both completed forms to PDF and email the two PDFs plus your photo to the Control & Mechatronics Lab functional mailbox: `mpebox11@nus.edu.sg`.
4. Wait for an email invitation and attend the approximately 20-minute laboratory safety orientation.
5. Wait for email confirmation that access is active before entering the laboratory to work.

## Form Downloads And Browser View

!!! warning "Sanitized reference copies only"
    Personal fields in the downloads have been replaced or left blank. Enter your own information and have your supervisor review the forms before submission. Completed forms contain personal information and must not be uploaded or committed to this Wiki repository.

### User Registration Form

[Download the sanitized user registration form (DOC)](../assets/forms/e2-01-04/user-registration-form-sanitized.doc)

The form requests:

- Name, matriculation or staff number, supervisor, project type, and attachment period.
- Contact and emergency-contact information.
- Completed safety training and completion dates.
- Acknowledgement of the laboratory-use guidelines, name, signature, and date.

The main laboratory rules require closed-toe footwear, no lone work after office hours, no food, permission for visitors, proper waste disposal, logbook entry after hours, equipment training before operation, and immediate reporting of incidents or equipment faults.

### Risk Assessment Form

[Download the sanitized risk assessment form (DOCX)](../assets/forms/e2-01-04/risk-assessment-form-sanitized.docx)

The download retains the E2-01-04 risk content for Franka Research 3, Aloha teleoperation, and dexterous-hand hardware work. Each applicant must update the people, dates, activity scope, action owners, and approvals for the actual project.

## Risk Assessment Reference

!!! warning "Project review required"
    The following content is a reference for existing hardware work and does not automatically approve a new project. Reassess the risks with your supervisor or laboratory staff whenever equipment, payloads, end effectors, fixtures, code, or experiment steps change.

### Activity Sequence

| Equipment/activity | Suggested sequence |
| --- | --- |
| Franka Research 3 | System setup, cable check, and power-on; programming, teaching, and calibration; trajectory testing; end-effector and payload handling; shutdown, recovery, and housekeeping |
| Aloha | System setup and power-on; teleoperation data collection; model training on a workstation; deployment and testing; shutdown and housekeeping |
| Dexterous-hand hardware | 3D-printed-parts post-processing; mechanical assembly; electrical wiring and PCB soldering; system integration; initial power-on and firmware/calibration; functional testing |

### Risks And Controls

??? info "Aloha 1: System setup and power-on (initial risk 4 → residual risk 2)"
    - **Hazards and consequences:** Electrical shock from cables or plugs and trips from loose cables may cause shock, falls, or bruises.
    - **Existing controls:** Inspect before use, use the correct power supply, and organize cables.
    - **Additional controls:** Secure cables, do not use damaged wires, and power off before connections or adjustments.
    - **Timing:** Before each use.

??? info "Aloha 2: Teleoperation data collection (initial risk 4 → residual risk 2)"
    - **Hazards and consequences:** Moving arms and grippers may cause pinching, collisions, bruises, or equipment damage.
    - **Existing controls:** Trained operators only, remain clear of the workspace, keep the emergency stop accessible, and start at low speed.
    - **Additional controls:** Define a safety zone, do not reach into the workspace during motion, and stop the system before adjustments.
    - **Timing:** Before and during operation.

??? info "Aloha 3: Deployment and testing (initial risk 4 → residual risk 2)"
    - **Hazards and consequences:** Unexpected robot motion or dropped objects may cause impact injuries and equipment damage.
    - **Existing controls:** Clear the workspace, test at low speed, and keep the emergency stop ready.
    - **Additional controls:** Have the supervisor present for initial tests, validate the program before running, and use one operator.
    - **Timing:** Before each deployment.

??? info "Franka 4: System setup and power-on (initial risk 6 → residual risk 3)"
    - **Hazards and consequences:** Electrical hazards, loose cables, incorrect connections, or unstable mounting may cause shock, falls, bruises, or equipment damage.
    - **Existing controls:** Inspect visually, use an approved power supply, keep the emergency stop accessible, and organize cables.
    - **Additional controls:** Secure cables, remove damaged wires from use, power off before connection or adjustment, and check robot-base and workbench stability.
    - **Timing:** Before each use.

??? info "Franka 5: Programming, teaching, and calibration (initial risk 6 → residual risk 3)"
    - **Hazards and consequences:** Incorrect programs, frames, trajectories, speed, or joint limits may cause unintended motion, pinching, collisions, or equipment damage.
    - **Existing controls:** Trained operators only, review code and trajectories, use low speed for the first test, and keep the emergency stop accessible.
    - **Additional controls:** Validate in simulation or slow mode, define a safety zone, do not reach into the workspace during motion, and have the supervisor present for the first run.
    - **Timing:** Before operation.

??? info "Franka 6: Robot motion and trajectory testing (initial risk 6 → residual risk 3)"
    - **Hazards and consequences:** Moving links and end effectors, unexpected restart during recovery, or collisions may cause crushing, pinching, impact injury, or equipment damage.
    - **Existing controls:** Remain clear, clear the workspace, use speed/force limits, and have one operator control the run.
    - **Additional controls:** Announce motion, use a safe stop before entering, wait for a full stop, and keep bystanders outside the workspace.
    - **Timing:** During operation.

??? info "Franka 7: End-effector and payload handling (initial risk 6 → residual risk 3)"
    - **Hazards and consequences:** Dropped tools or payloads, loose fasteners, incorrect payload/TCP/centre-of-mass settings, or sharp edges may cause hand or foot injuries, cuts, and equipment damage.
    - **Existing controls:** Check mass and mounting, use suitable fasteners, support payloads during installation, and avoid pinch points.
    - **Additional controls:** Verify TCP, payload, and centre-of-mass settings; use eye protection or gloves as needed; do not exceed limits; and remove loose objects.
    - **Timing:** Before payload testing.

??? info "Franka 8: Shutdown, recovery, and housekeeping (initial risk 6 → residual risk 3)"
    - **Hazards and consequences:** Residual motion, energized controllers or cables, improper emergency unlocking, and loose tools or cables may cause pinching, shock, trips, or equipment damage.
    - **Existing controls:** Stop the program, return to a safe pose, power down as required, and keep the area tidy.
    - **Additional controls:** Emergency unlocking only when required and by trained personnel, support the arm before unlocking, store tools and cables, and report faults immediately.
    - **Timing:** After each use.

??? info "Dexterous hand 9: 3D-printed-parts post-processing (initial risk 4 → residual risk 2)"
    - **Hazards and consequences:** Sharp edges, plastic or resin dust, and snapping thin structures may cause cuts, eye irritation, respiratory discomfort, or component damage.
    - **Existing controls:** Wear cut-resistant gloves, sand in a ventilated area or fume hood, and hold parts near thicker sections.
    - **Additional controls:** Wear safety goggles and an N95 dust mask, use a deburring tool instead of bare blades, and support thin parts with soft foam.
    - **Timing:** Before assembly.

??? info "Dexterous hand 10: Mechanical assembly (initial risk 6 → residual risk 2)"
    - **Hazards and consequences:** Joint pinch points, tendon snapback, flying screws or springs, and incorrect gear meshing may injure hands or eyes or damage the mechanism.
    - **Existing controls:** Use tweezers and needle-nose pliers, increase tendon tension gradually, and inspect gear alignment before tightening.
    - **Additional controls:** Wear safety glasses, use a magnetic tray, apply low-strength threadlocker, and hold the palm base in a fixture.
    - **Timing:** During assembly.

??? info "Dexterous hand 11: Electrical wiring and PCB soldering (initial risk 6 → residual risk 2)"
    - **Hazards and consequences:** Soldering-iron burns, solder bridges, reversed polarity, and ESD may cause burns, board damage, controller failure, or fire.
    - **Existing controls:** Use a soldering station with a tip rest, disconnect power, verify pinouts, and wear an ESD strap.
    - **Additional controls:** Use a fire-resistant mat and heat-shrink tubing, check continuity before power-on, and keep a small fire extinguisher nearby.
    - **Timing:** Before power-on.

??? info "Dexterous hand 12: System integration (initial risk 4 → residual risk 2)"
    - **Hazards and consequences:** Dropping the hand, connector strain, or cables tangled around joints may cause equipment damage, broken pins, intermittent signals, or trips.
    - **Existing controls:** Support the hand with a counterbalanced arm or adjustable stand, add strain-relief loops, and route cables away from joints.
    - **Additional controls:** Use two people for mounting, use locking connectors, and perform a slow full-joint cable sweep before final tightening.
    - **Timing:** During integration.

??? info "Dexterous hand 13: Initial power-on, firmware, and calibration (initial risk 6 → residual risk 2)"
    - **Hazards and consequences:** Twitching or rapid homing, over-current, finger collisions, or reversed motion may cause pinching, gear or driver damage, and detachment from the mount.
    - **Existing controls:** Limit current/torque to 30% of maximum, enable one finger at a time, and place soft foam around the workspace.
    - **Additional controls:** Keep an emergency stop or software kill switch accessible, home at 20% speed first, monitor joint feedback, and enable software position limits before torque.
    - **Timing:** During initial boot-up.

??? info "Dexterous hand 14: Functional testing (initial risk 6 → residual risk 2)"
    - **Hazards and consequences:** Dropped objects, fingertip collisions, or sustained over-torque may injure feet, damage equipment, wear fingertips, overheat motors, or project objects.
    - **Existing controls:** Start with soft objects no heavier than 50 g, increase payload gradually, define a software safety workspace, and monitor motor temperature.
    - **Additional controls:** Install a transparent shield, announce motion, delay high-torque engagement by one second, and perform a simulation dry run when available.
    - **Timing:** Before each test run.

### Risk Matrix

Risk is `likelihood × severity`, with each factor rated from 1 to 5:

| Risk score | Required decision |
| --- | --- |
| `< 5` | Risk acceptable |
| `5–14` | Consider additional risk controls |
| `> 14` | Additional risk controls required |

## Verification

- Confirm that all applicable training is complete and dates are recorded.
- Confirm that both PDF forms and the personal photo were sent to the functional mailbox.
- Confirm attendance at the safety orientation and receipt of the access-activation email.
- Before first use, review project risk controls and equipment-operation requirements with your supervisor or laboratory staff.

## Troubleshooting

- If a Canvas course is unavailable, search All Courses by course code and ask laboratory staff whether the course has changed.
- CHRS LMS courses are staff-only; students do not need to complete courses marked Staff only.
- If the browser cannot open a `.doc` or `.docx`, download it and use a compatible office application.
- If the orientation or activation email does not arrive, check junk mail and follow up through the functional laboratory mailbox.

<p class="wiki-meta">Owner: Onboarding Maintainer · Last verified: 2026-08-08</p>
