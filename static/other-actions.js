window.onload = function () {
  var ids = ["education", "experience", "projects", "certifications"];
  ids.forEach(function (id) {
    var wrapper = document.getElementById(id);
    if (wrapper) {
      var anchors = wrapper.getElementsByTagName("a");
      for (var i = 0; i < anchors.length; i++) {
        anchors[i].setAttribute("target", "_blank");
      }
    }
  });
};

document.addEventListener("DOMContentLoaded", function () {
  const timelineEvents = document.querySelectorAll(".timeline-event");

  const pixelsPerMonth = 10; // Adjust as needed
  let maxEndDate = new Date(2013, 0); // Initialize with the new start of the timeline

  timelineEvents.forEach((event) => {
    const startDate = event.getAttribute("data-start");
    const endDate = event.getAttribute("data-end");

    const start = new Date(startDate);
    const end = new Date(endDate);

    // Update the maximum end date
    if (end > maxEndDate) {
      maxEndDate = end;
    }

    let topOffset;
    let adjustedStart = start;

    if (start < new Date(2013, 0)) {
      adjustedStart = new Date(2013, 0);
      topOffset = 0;

      // Add the original start date display
      const startLabel = document.createElement("div");
      startLabel.className = "start-date";
      startLabel.textContent = startDate;
      event.insertBefore(startLabel, event.firstChild);
      event.style.paddingTop = "30px"; // Add space for the start date
    } else {
      topOffset =
        ((start.getFullYear() - 2013) * 12 + start.getMonth()) * pixelsPerMonth;
    }

    // Calculate the height based on the adjusted start date
    const months =
      (end.getFullYear() - adjustedStart.getFullYear()) * 12 +
      (end.getMonth() - adjustedStart.getMonth());

    const height = months * pixelsPerMonth;
    event.style.height = height + "px";
    event.style.top = topOffset + "px";
  });

  // Adjust the timeline container height
  const timelineContainer = document.querySelector(".timeline");
  const totalMonths =
    (maxEndDate.getFullYear() - 2013) * 12 + maxEndDate.getMonth();
  const timelineHeight = totalMonths * pixelsPerMonth;
  timelineContainer.style.height = timelineHeight + "px";

  // Adjust the timeline line height
  const timelineLine = document.querySelector(".timeline-line");
  timelineLine.style.height = timelineHeight + "px";
});
