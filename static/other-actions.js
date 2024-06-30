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
  const timelineLine = document.querySelector(".timeline-line");

  const startYear = 2013;
  const endYear = 2024;

  const pixelsPerMonth = 10; // Adjust as needed
  let maxEndDate = new Date(endYear, 0); // Set the max end date to the last year

  // Add year markers dynamically
  for (let year = startYear; year <= endYear; year++) {
    const yearMarker = document.createElement("div");
    yearMarker.className = "year-marker";
    yearMarker.textContent = year;
    const yearOffset = (year - startYear) * 12 * pixelsPerMonth;
    yearMarker.style.top = yearOffset + "px";
    timelineLine.appendChild(yearMarker);
  }

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

    if (start < new Date(startYear, 0)) {
      adjustedStart = new Date(startYear, 0);
      topOffset = 0;

      // Add the original start date display
      const startLabel = document.createElement("div");
      startLabel.className = "start-date";
      startLabel.textContent = startDate;
      event.insertBefore(startLabel, event.firstChild);
      event.style.paddingTop = "30px"; // Add space for the start date
    } else {
      topOffset =
        ((start.getFullYear() - startYear) * 12 + start.getMonth()) *
        pixelsPerMonth;
    }

    // Calculate the height based on the adjusted start date
    const months =
      (end.getFullYear() - adjustedStart.getFullYear()) * 12 +
      (end.getMonth() - adjustedStart.getMonth());

    const height = Math.max(months * pixelsPerMonth, 100); // Ensure a minimum height
    event.style.height = height + "px";
    event.style.top = topOffset + "px";
  });

  // Adjust the timeline container height
  const timelineContainer = document.querySelector(".timeline");
  const totalMonths =
    (maxEndDate.getFullYear() - startYear) * 12 + maxEndDate.getMonth();
  const timelineHeight = totalMonths * pixelsPerMonth;
  timelineContainer.style.height = timelineHeight + "px";

  // Adjust the timeline line height
  timelineLine.style.height = timelineHeight + "px";
});
