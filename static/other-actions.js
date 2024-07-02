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

  const startYear = 2013;
  let endYear = startYear; // Initialize endYear as startYear for comparison

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
        ((start.getFullYear() - startYear) * 12 + start.getMonth()) * 10; // assuming pixelsPerMonth is 10
    }

    const months =
      (end.getFullYear() - adjustedStart.getFullYear()) * 12 +
      (end.getMonth() - adjustedStart.getMonth());
    const height = Math.max(months * 10, 100); // Ensure a minimum height
    event.style.height = height + "px";
    event.style.top = topOffset + 30 + "px"; // Adjust for top padding
  });

  // Add year markers and line segments dynamically
  for (let year = startYear; year <= endYear; year++) {
    const yearMarker = document.createElement("div");
    yearMarker.className = "year-marker";
    yearMarker.textContent = year;
    const yearOffset = (year - startYear) * 12 * 10; // 10 is pixelsPerMonth
    yearMarker.style.top = yearOffset + 30 + "px"; // Adjust the position
    timelineContainer.appendChild(yearMarker);

    if (year < endYear) {
      const lineSegment = document.createElement("div");
      lineSegment.className = "timeline-line";
      lineSegment.style.top = yearOffset + 30 + 7 + "px"; // Adjust to place the marker in the middle of the gap
      lineSegment.style.height = 12 * 10 - 14 + "px"; // Adjust to leave space for the year marker
      timelineContainer.appendChild(lineSegment);
    }
  }

  // Adjust the timeline container height
  const totalMonths = (endYear - startYear) * 12 + 12; // Extend the timeline to December of the end year
  const timelineHeight = totalMonths * 10;
  timelineContainer.style.height = timelineHeight + 0 + "px"; // Adjust for top padding
});
