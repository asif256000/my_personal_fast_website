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
  let endMonth = 0;
  let totalContainerHeight = 0;
  const pixelsPerMonth = 10;
  const topOffset = 60; // Increased offset by 60px

  function calculatePosition(event) {
    const startDate = event.getAttribute("data-start");
    let endDate = event.getAttribute("data-end");

    let start = new Date(startDate);
    start.setDate(15); // Set the date to the middle of the month
    const end = new Date(endDate);
    end.setDate(15); // Set the date to the middle of the month
    console.log("end", endDate, end.getUTCMonth(), end.toISOString());

    // Update the maximum endYear and corresponding endMonth found so far
    if (end.getUTCFullYear() > endYear) {
      endYear = end.getUTCFullYear();
      endMonth = end.getUTCMonth();
    } else if (
      end.getUTCFullYear() === endYear &&
      end.getUTCMonth() > endMonth
    ) {
      endMonth = end.getUTCMonth();
    }
    console.log("endYear", endYear, "endMonth", endMonth);

    // Cap the start date to the base year if it's earlier
    if (start.getUTCFullYear() < baseYear && start.getUTCMonth() < 6) {
      start = new Date(baseYear - 1, 7);
    }

    const startMonthsFromBase =
      (start.getUTCFullYear() - baseYear) * 12 + start.getUTCMonth();
    const endMonthsFromBase =
      (end.getUTCFullYear() - baseYear) * 12 + end.getUTCMonth();
    const monthsDuration = Math.max(
      endMonthsFromBase - startMonthsFromBase + 1,
      1
    );

    const height = monthsDuration * pixelsPerMonth;
    const topPosition = startMonthsFromBase * pixelsPerMonth + topOffset + 60;

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
  endMonth = endMonth + 2;

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

  const dashedLineSegment = document.createElement("div");
  dashedLineSegment.className = "timeline-line dotted";
  dashedLineSegment.style.top = topOffset - 7 + "px";
  dashedLineSegment.style.height = 6 * pixelsPerMonth + "px";
  timelineContainer.appendChild(dashedLineSegment);
  console.log(endYear, endMonth);

  for (let year = baseYear; year <= endYear; year++) {
    const yearOffset = (year - baseYear) * 12 * pixelsPerMonth;

    const yearMarker = document.createElement("div");
    yearMarker.className = "year-marker";
    yearMarker.textContent = year;
    yearMarker.style.top = yearOffset + topOffset + 60 + "px";
    timelineContainer.appendChild(yearMarker);

    const lineSegment = document.createElement("div");
    let last_months = 12;
    if (year === endYear) {
      lineSegment.className = "timeline-line dotted";
      last_months = endMonth + 1;
    } else {
      lineSegment.className = "timeline-line";
    }
    lineSegment.style.top = yearOffset + topOffset + 67 + "px";
    lineSegment.style.height = last_months * pixelsPerMonth - 14 + "px";
    timelineContainer.appendChild(lineSegment);
  }

  timelineContainer.style.height =
    ((endYear - baseYear) * 12 + endMonth + 1) * pixelsPerMonth +
    topOffset +
    60 +
    "px";
});
