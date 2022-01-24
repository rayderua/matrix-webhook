"""Formatters for matrix webhook."""
from . import utils


def grafana(data, headers):
    """Pretty-print a grafana notification."""
    text = ""
    if "title" in data:
        text = "#### " + data["title"] + "\n"
    if "message" in data:
        text = text + data["message"] + "\n\n"
    if "evalMatches" in data:
        for match in data["evalMatches"]:
            text = text + "* " + match["metric"] + ": " + str(match["value"]) + "\n"
    data["body"] = text
    return data


def github(data, headers):
    """Pretty-print a github notification."""
    # TODO: Write nice useful formatters. This is only an example.
    if headers["X-GitHub-Event"] == "push":
        pusher, ref, a, b, c = [
            data[k] for k in ["pusher", "ref", "after", "before", "compare"]
        ]
        pusher = f"[@{pusher['name']}](https://github.com/{pusher['name']})"
        data["body"] = f"{pusher} pushed on {ref}: [{b} → {a}]({c}):\n\n"
        for commit in data["commits"]:
            data["body"] += f"- [{commit['message']}]({commit['url']})\n"
    else:
        data["body"] = "notification from github"
    data["digest"] = headers["X-Hub-Signature-256"].replace("sha256=", "")
    return data


def slack(data, headers):
    """Pretty-print a slack notification."""
    text = ""
    if "text" in data:
        text = text + "<div>" + utils.format_url(data["text"]) + "</div>\n"
    if "attachments" in data and len(data["attachments"]):
        for attachment in data["attachments"]:
            text = text + "<div>"
            if "title_link" in attachment and "title" in attachment:
                text = text + "<h4><a href=\"" + attachment["title_link"] + "\">" + attachment["title"] + "</a></h4>\n"
            elif "title" in attachment:
                text = text + "<h4>" + utils.format_url(attachment["title"]) + "</h4>\n"
            if "text" in attachment:
                text = text + utils.format_url(attachment["text"]) + "\n"

            if "fields" in attachment and len(attachment["fields"]):
                for field in attachment["fields"]:
                    text = text + "<div>"
                    if "title" in field:
                        text = text + "<h5>" + utils.format_url(field["title"]) + "</h5>\n"
                    if "value" in field:
                        text = text + utils.format_url(str(field["value"])) + "\n"
                    text = text + "</div>"
            text = text + "</div>"
    data["body"] = text
    return data


def raw(data, headers):
    """Raw print."""
    from json import dumps
    data["body"] = "### Data: \n```json\n" + dumps(data, indent=2) + "\n```\n"
    return data
