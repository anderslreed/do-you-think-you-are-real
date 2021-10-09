function check_load() {
    const request = new XMLHttpRequest();
    request.open("POST", "/content");
    const curernt_hour = new Date().getHours()
    const request_json = JSON.stringify({"hour": curernt_hour});
    request.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    request.onreadystatechange = function() {
        if (request.readyState === 4 && request.status === 200) {
            response_values = JSON.parse(request.responseText);
            const css_link = document.createElement("link");
            css_link.rel = "stylesheet"
            css_link.type = "text/css"
            css_link.href = response_values["css_file"]
            document.head.title = response_values["title"]
            document.head.appendChild(css_link);
            document.body.innerHTML = response_values["body"];
        }
    }
    request.send(request_json);
}