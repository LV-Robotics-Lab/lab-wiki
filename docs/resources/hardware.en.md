# Physical-Hardware Resource Center

!!! danger "Public pages must not store credentials"
    Maintainer-approved Google Drive, Feishu, Yuque, and vendor-document links, as well as hostnames, tailnet IPs, GPU configurations, and equipment locations, may be documented in the Wiki. Never publish passwords, API keys, access tokens, private keys, Auth IDs, cookies, unattended-access passwords, or request headers containing them.

## Purpose

Help Physical Systems members verify hardware identity, documentation versions, safety status, and authorization before booking, powering, developing with, or returning equipment.

## Group Scope

| Group | Relationship | How this page applies |
|---|---|---|
| Physical Systems | Parent group | Owns physical robots, teleoperation, collection, and hardware integration |
| Ego | Subgroup of Physical Systems | Checks first-person collection, human-motion input, and teleoperation equipment |
| Dexterous Hands | Subgroup of Physical Systems | Checks dexterous hands, arm end effectors, control SDKs, and teleoperation links |
| Tactile | Subgroup of Physical Systems | Checks tactile sensors, acquisition boards, calibration, and synchronization links |
| Simulation | Peer of Physical Systems | Receives verified models, calibration, and device parameters through controlled interfaces without directly occupying hardware |
| World Models | Peer of Physical Systems | Receives approved physical-robot data and metadata through the data-management process without directly requesting device-control privileges |

!!! note "Confirm ownership on site"
    The Recommended Group column below is for resource discovery; it does not grant ownership or operating authorization. Cross-group use still requires approval from the equipment maintainer.

## Prerequisites

- Obtain approval from the project owner and equipment maintainer, and complete required safety training.
- Confirm the model, current state, maintainer, booking window, and allowed purpose in the controlled asset register.
- Read the vendor safety information and laboratory SOP matching the current hardware and firmware version.
- Confirm the data destination, responsible member, expected occupation period, and incident-reporting path.

## Pre-Use Verification Checklist

### Identity and State

- Match the asset label to the product, model, handedness/end-effector configuration, and accessory list.
- Verify live device state, maintenance history, booking conflicts, and recent incidents in the controlled system; the public page does not display live inventory.
- When collecting necessary appearance or wiring evidence, avoid serial numbers and on-screen credentials. Hostnames/IPs may be recorded, but do not show them together with passwords, tokens, or account credentials in the same screenshot.

### Safety and Site

- Check the emergency stop, limits, power, fixtures, cables, collision zone, and on-site safety observer.
- Complete a smoke test with the lowest safe speed/torque and smallest motion range on first power-up.
- Do not power on remotely, start a trajectory, or bypass emergency-stop or limit controls before on-site safety verification.

### Software and Protocol

- Record client, SDK, firmware, model, and communication-protocol versions and confirm compatibility with the target device.
- Run a read-only status query or the vendor's minimal example before project code.
- Never place shared passwords, device-account credentials, API keys, access tokens, private keys, or unattended-access passwords in scripts, notebooks, Issues, or log screenshots.

### Data and Return

- Before collection, confirm time synchronization, coordinate frames, calibration files, data format, and storage destination.
- After the experiment, stop motion, power down, restore accessories, record the end of occupation, and report anomalies.
- Store raw data, calibration, and minimum metadata according to [Research Data Storage and Archiving](data-management.en.md).

## Resource Catalog

| Hardware or resource | Recommended group | Verify before use | Safe entry point |
|---|---|---|---|
| RealHand / LinkerHand | Dexterous Hands | Model, handedness, firmware, and teleoperation-script version | [RealHand resource folder](https://drive.google.com/drive/folders/1bDQFkxWZW1SapAQazwENOSOL_vWyM9Ti?usp=sharing); [LinkerHand teleoperation Python](https://gitee.com/ericbrunt/linkerhand_telop_python) |
| AgileX NERO / TRACER | Shared Physical Systems | Arm/base model, emergency stop, control mode, SDK, and communication-protocol version | [NERO product page](https://global.agilex.ai/products/nero); [NERO user manual](https://agilexsupport.yuque.com/staff-hso6mo/alxgtf/air57k7k3nhgeuxb?singleDoc=); [support document 1](https://agilexsupport.yuque.com/staff-hso6mo/toh64r/ad5tfngbirdvhunm?singleDoc=); [support document 2](https://agilexsupport.yuque.com/staff-hso6mo/toh64r/tcpvae9wrb5xnivn?singleDoc=); [TRACER 2.0 user manual](https://agilexsupport.yuque.com/staff-hso6mo/toh64r/yg09k9oh1b4b046x?singleDoc#%20%E3%80%8A%E9%99%84%E4%BB%B62-TRACER%202.0%20%E7%94%A8%E6%88%B7%E6%89%8B%E5%86%8C%E3%80%8B); [support document 4](https://agilexsupport.yuque.com/staff-hso6mo/alxgtf/km95una15ctk4b17?singleDoc=) |
| Daimon / TacClaw | Tactile and Dexterous Hands | Main board, sensors, calibration revision, acquisition link, and connection authorization | [Daimon hardware resource folder](https://drive.google.com/drive/folders/1gOMqA2WjBhTcx3Af2x-t1vo9qJFS78E8?usp=sharing) |
| UDEXREAL / HigVR data gloves | Ego and Dexterous Hands | Handedness, size, firmware, calibration, and time synchronization | [UDEXREAL usage guide](https://hs7ghlauag.feishu.cn/docx/BlqKdFOSeoFQG1xzbV9ccNMMnzc); [HigVR User Manual](https://higvr.com/en-cn/pages/user-manual) |
| WUJI Hand | Dexterous Hands | Product generation, handedness, power, SDK/ROS compatibility, and safety constraints | [WUJI Hand Documentation Center](https://docs.wuji.tech/docs/zh/wuji-hand/latest/) |
| Franka / GELLO | Ego and Dexterous Hands | Arm identity, controller state, end effector, limits, and teleoperation link | [Franka GELLO single-arm guide](https://docs.google.com/document/d/13ILD-wukxa0Szt1wgoUBytA2SqVOcGDsZ0kLR67Po7M/edit?usp=drivesdk) |
| YAM / i2rt | Shared Physical Systems | Model, end effector, API/SDK revision, calibration, and safety boundary | [YAM / YUM resource folder](https://drive.google.com/drive/folders/1et1BCPRL1p-zUde3mMlmilPYLowDVnn3); [i2rt Python API](https://github.com/i2rt-robotics/i2rt) |
| LeRobot | Physical Systems and Simulation | Data format, hardware adapters, version, and example configuration | [LeRobot usage tutorial](https://zihao-ai.feishu.cn/wiki/TS6swApHbinx01kHDi5cf5n5n8c) |
| NERO Arm Communication Protocol V1.2.1 | Shared Physical Systems | Applicable model, revision, CAN standard, bit rate, and data format | Request as a controlled technical attachment; do not reproduce it in the public Wiki |

!!! info "Link permissions"
    Some Drive, Feishu, Yuque, or Google Docs links may require login or authorization from the resource owner. The Wiki does not store accounts, cookies, passwords, or tokens used to open them.

## Supporting Management Resources

- Hardware resource directory: `<HARDWARE_RESOURCE_DIRECTORY_URL>`
- Asset and state register: `<HARDWARE_ASSET_REGISTER_URL>`
- Booking and occupation log: `<HARDWARE_BOOKING_URL>`
- Protocol and calibration archive: `<HARDWARE_PROTOCOL_ARCHIVE_URL>`
- Maintenance and incident log: `<HARDWARE_MAINTENANCE_LOG_URL>`
- Contact directory: `<CONTROLLED_CONTACT_DIRECTORY_URL>`

## Procedure

1. Use the project task and Group Scope above to identify the required hardware or documentation.
2. Confirm device state and maintainer in the asset register, then submit the booking, purpose, period, and on-site responsible member.
3. Read this page's resource links first; request additional permissions for manuals, protocols, calibration, and access from the resource owner or equipment maintainer.
4. Complete identity, safety, version, and data checks from the pre-use checklist and retain necessary controlled records.
5. Pass the minimum smoke test before the formal experiment; stop on any anomaly, preserve evidence, and notify the maintainer.
6. Complete power-down, return, data storage, and state updates after the experiment.

## Verification

- The product, model, accessories, and documentation revision match the physical device.
- Booking, operating authorization, and on-site safety conditions are confirmed.
- The minimum smoke test passes with no unexplained error or out-of-bound event.
- Raw data, calibration, and experiment metadata are written to an approved storage location.
- No real password, API key, token, private key, Auth ID, cookie, unattended-access password, or device serial number appears in the Wiki or public repository.

## Troubleshooting

- Device state or ownership is unclear: pause the booking and ask the Hardware Resources Maintainer to verify it on site.
- A public link fails: record the product and page name and submit a maintenance request; do not substitute an untrusted mirror.
- Protocol or SDK does not match the device: stop control and verify the model, firmware, applicable protocol scope, and maintenance record.
- Connection fails: check power, cables, emergency stop, and the official minimal example before controlled network and permission checks.
- A key, token, password, private key, Auth ID, cookie, or unattended-access password is exposed: stop using it and notify the maintainer for revocation and rotation; never paste the value into an Issue.
- Hardware appears damaged: stop, power down, isolate the device, and attach redacted evidence to the maintenance record.

## Maintenance

- Owner: Hardware Resources Maintainer
- Contact: `<CONTROLLED_CONTACT_DIRECTORY_URL>`
- Last verified: 2026-08-03
