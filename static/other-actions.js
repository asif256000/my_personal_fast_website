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
  const timelineContainer = document.querySelector(".timeline");

  const startYear = 2014;
  let endYear = startYear;
  let pixelsPerMonth = 10;

  timelineEvents.forEach((event) => {
    const endDate = event.getAttribute("data-end");
    const end = new Date(endDate);

    // Update the endYear if this event ends later than the current endYear
    if (end.getFullYear() > endYear) {
      endYear = end.getFullYear();
    }

    const startDate = event.getAttribute("data-start");
    const start = new Date(startDate);

    let topOffset = 0;
    let adjustedStart = start;

    if (start < new Date(startYear, 0)) {
      adjustedStart = new Date(startYear, 0);
    } else {
      topOffset =
        ((start.getFullYear() - startYear) * 12 + start.getMonth()) *
        pixelsPerMonth;
    }

    const months =
      (end.getFullYear() - adjustedStart.getFullYear()) * 12 +
      (end.getMonth() - adjustedStart.getMonth());
    const height = Math.max(months * pixelsPerMonth, 100);
    event.style.height = height + "px";
    event.style.top = topOffset + 30 + "px"; // Adjust for top padding
  });

  // Add year markers and line segments dynamically
  for (let year = startYear; year <= endYear; year++) {
    const yearMarker = document.createElement("div");
    yearMarker.className = "year-marker";
    yearMarker.textContent = year;
    const yearOffset = (year - startYear) * 12 * pixelsPerMonth;
    yearMarker.style.top = yearOffset + 30 + "px"; // Adjust the position
    timelineContainer.appendChild(yearMarker);

    if (year < endYear) {
      const lineSegment = document.createElement("div");
      lineSegment.className = "timeline-line";
      lineSegment.style.top = yearOffset + 30 + 7 + "px"; // Adjust to place the marker in the middle of the gap
      lineSegment.style.height = 12 * pixelsPerMonth - 14 + "px";
      timelineContainer.appendChild(lineSegment);
    }
  }

  // Adjust the timeline container height
  const totalMonths = (endYear - startYear) * 12 + 12; // Extend the timeline to December of the end year
  const timelineHeight = totalMonths * pixelsPerMonth;
  timelineContainer.style.height = timelineHeight + 0 + "px"; // Adjust for top padding
});
