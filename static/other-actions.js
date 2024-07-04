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
  const pixelsPerMonth = 10;
  const topOffset = 60; // Increased offset by 60px

  function calculatePosition(event) {
    const startDate = event.getAttribute("data-start");
    let endDate = event.getAttribute("data-end");

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

    const startMonthsFromBase =
      (start.getFullYear() - baseYear) * 12 + start.getMonth();
    const endMonthsFromBase =
      (end.getFullYear() - baseYear) * 12 + end.getMonth();
    const monthsDuration = Math.max(
      endMonthsFromBase - startMonthsFromBase + 1,
      1
    );

    const height = monthsDuration * pixelsPerMonth;
    const topPosition = startMonthsFromBase * pixelsPerMonth + topOffset;

    event.style.top = `${topPosition}px`;
    event.style.height = `${height}px`;

    if (monthsDuration < 4) {
      const pTag = event.querySelector(".content p");
      if (pTag) {
        pTag.style.display = "none";
      }
      event.setAttribute("data-end", "");
    }
  }

  timelineEvents.forEach(calculatePosition);
  timelineEvents.forEach((event) => {
    event.addEventListener("mouseenter", function () {
      const detailBox = this.querySelector(".detail-box");
      if (detailBox) {
        const boxRect = detailBox.getBoundingClientRect();
        if (boxRect.right > window.innerWidth) {
          detailBox.style.left = "auto";
          detailBox.style.right = "100%"; // Flip to the left
        } else if (boxRect.left < 0) {
          detailBox.style.right = "auto";
          detailBox.style.left = "100%"; // Flip to the right if it goes out of the left side of the viewport
        }
      }
    });
  });

  for (let year = baseYear; year <= endYear; year++) {
    const yearMarker = document.createElement("div");
    yearMarker.className = "year-marker";
    yearMarker.textContent = year;
    const yearOffset = (year - baseYear) * 12 * pixelsPerMonth;
    yearMarker.style.top = yearOffset + topOffset + "px";
    timelineContainer.appendChild(yearMarker);

    const lineSegment = document.createElement("div");
    lineSegment.className = "timeline-line";
    lineSegment.style.top = yearOffset + topOffset + 7 + "px";
    lineSegment.style.height = 12 * pixelsPerMonth - 14 + "px";
    timelineContainer.appendChild(lineSegment);
  }

  timelineContainer.style.height =
    (endYear - baseYear + 1) * 12 * pixelsPerMonth + topOffset + "px";
});
