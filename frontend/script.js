function showTab(tabId, element){

    document
    .querySelectorAll(".content")
    .forEach(tab=>{
        tab.classList.add("hidden");
    });

    document
    .getElementById(tabId)
    .classList.remove("hidden");

    document
    .querySelectorAll(".tab")
    .forEach(tab=>{
        tab.classList.remove("active-tab");
    });

    element.classList.add("active-tab");
}

let currentUser = "None";

async function login(){

    const username =
    document.getElementById("username").value;

    currentUser = username;

    document.getElementById(
        "currentUser"
    ).innerText = username;

    addTimeline(
        `${username} logged in`
    );

    loadDashboard();
}

async function uploadFile(){

    const file =
    document.getElementById("filename").value;

    addThreat(
        "Suspicious File Upload",
        `User uploaded ${file}`
    );
}

async function adminAccess(){

    addThreat(
        "Unauthorized Admin Access",
        "User attempted admin access"
    );
}

async function scanNetwork(){

    addThreat(
        "Network Reconnaissance",
        "User performed a network scan"
    );
}

let threats = [];

let timeline = [];

function addThreat(type, description){

    threats.push({
        type:type,
        description:description
    });

    timeline.push(description);

    loadDashboard();
}

function addTimeline(event){

    timeline.push(event);

    loadDashboard();
}

function loadDashboard(){

    document.getElementById(
        "threatCount"
    ).innerText =
    threats.length;

    document.getElementById(
        "riskScore"
    ).innerText =
    threats.length * 15;

    const threatContainer =
    document.getElementById(
        "threatsContainer"
    );

    threatContainer.innerHTML = "";

    threats.forEach(threat=>{

        threatContainer.innerHTML += `

        <div class="threat">

            <h3>${threat.type}</h3>

            <p>${threat.description}</p>

        </div>

        `;
    });

    const timelineDiv =
    document.getElementById("timeline");

    timelineDiv.innerHTML = "";

    timeline
    .slice()
    .reverse()
    .forEach(event=>{

        timelineDiv.innerHTML += `
            <p>${event}</p>
        `;
    });

    const aiPanel =
    document.getElementById("aiPanel");

    if(threats.length===0){

        aiPanel.innerHTML = `
        Environment Secure
        `;

    }else{

        aiPanel.innerHTML = `
        <b>AI Assessment</b><br><br>

        ${threats.length}
        suspicious activities detected.<br><br>

        Recommended Actions:

        <ul>
            <li>Review employee actions</li>
            <li>Verify access permissions</li>
            <li>Investigate uploaded files</li>
            <li>Monitor network activity</li>
        </ul>
        `;
    }
}

loadDashboard();