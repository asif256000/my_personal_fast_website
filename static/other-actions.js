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

  const baseYear = 2014;
  let endYear = baseYear;
  let pixelsPerMonth = 10;

  function calculatePosition(event) {
    const startDate = event.getAttribute("data-start");
    const endDate = event.getAttribute("data-end");

    let start = new Date(startDate);
    const end = new Date(endDate);

    // Update the maximum end year found so far.
    if (end.getFullYear() > endYear) {
      endYear = end.getFullYear();
    }

    // Cap the start date to the base year if it's earlier
    if (start.getFullYear() < baseYear) {
      start = new Date(baseYear, 0); // January of the base year
    }

    // Calculate the offset for the start month from the base year
    const startMonthsFromBase =
      (start.getFullYear() - baseYear) * 12 + start.getMonth();

    // Calculate the offset for the end month from the base year
    const endMonthsFromBase =
      (end.getFullYear() - baseYear) * 12 + end.getMonth();

    // Ensure that the start month is not greater than the end month
    const monthsDuration = Math.max(
      endMonthsFromBase - startMonthsFromBase + 1,
      1
    );

    // Set the height of the box based on number of months
    const height = monthsDuration * pixelsPerMonth;

    // Set the top position of the box
    const topPosition = startMonthsFromBase * pixelsPerMonth + 30; // 30px for the offset

    event.style.top = `${topPosition}px`;
    event.style.height = `${height}px`;
  }

  // Calculate positions for each event
  timelineEvents.forEach(calculatePosition);

  // Add year markers and adjust container height
  for (let year = baseYear; year <= endYear; year++) {
    const yearMarker = document.createElement("div");
    yearMarker.className = "year-marker";
    yearMarker.textContent = year;
    const yearOffset = (year - baseYear) * 12 * pixelsPerMonth;
    yearMarker.style.top = yearOffset + 30 + "px"; // Adjust the position
    timelineContainer.appendChild(yearMarker);

    // Line segments for each year
    const lineSegment = document.createElement("div");
    lineSegment.className = "timeline-line";
    lineSegment.style.top = yearOffset + 30 + 7 + "px";
    lineSegment.style.height = 12 * pixelsPerMonth - 14 + "px";
    timelineContainer.appendChild(lineSegment);
  }

  // Set the height of the timeline container
  const totalMonths = (endYear - baseYear + 1) * 12;
  timelineContainer.style.height = totalMonths * pixelsPerMonth + 30 + "px"; // Adjust for top padding
});
