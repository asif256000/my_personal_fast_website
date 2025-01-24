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
  const allSelectedItems = document.querySelectorAll(".selected-item");

  // Toggle the navbar menu
  function toggleNavbar(event) {
    const selectedItem = event.target.closest(".selected-item");
    // const nav = selectedItem.closest("nav");
    // const navMenu = nav.querySelector("ul");
    const navMenu = selectedItem.nextElementSibling;
    const isExpanded = navMenu.classList.toggle("active");

    if (isExpanded) {
      selectedItem.innerHTML = selectedItem.innerHTML.replaceAll("▼", "▲");
    } else {
      selectedItem.innerHTML = selectedItem.innerHTML.replaceAll("▲", "▼");
    }
  }

  // Collapse all navbars when clicking outside
  document.addEventListener("click", function (event) {
    const allNavMenus = document.querySelectorAll("nav ul");
    let clickedInside = false;

    // Check if the click happened inside any nav
    allNavMenus.forEach((navMenu) => {
      if (navMenu.contains(event.target)) {
        clickedInside = true;
      }
    });

    allSelectedItems.forEach((selectedItem) => {
      if (selectedItem.contains(event.target)) {
        clickedInside = true;
      }
    });

    if (!clickedInside) {
      allNavMenus.forEach((navMenu) => {
        if (navMenu.classList.contains("active")) {
          navMenu.classList.remove("active");
          const associatedSelectedItem = navMenu
            .closest("nav")
            .querySelector(".selected-item");
          associatedSelectedItem.innerHTML =
            associatedSelectedItem.innerHTML.replaceAll("▲", "▼");
        }
      });
    }
  });

  // Attach the toggleNavbar function to the selected items
  allSelectedItems.forEach((selectedItem) => {
    selectedItem.addEventListener("click", toggleNavbar);
  });
});

document.addEventListener("DOMContentLoaded", function () {
  // Update the timeline event positions
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
    let end;
    if (endDate != null) {
      end = new Date(endDate);
    } else {
      end = new Date();
    }

    end.setDate(15); // Set the date to the middle of the month

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

    // Cap the start date to the base year if it's earlier
    if (start.getUTCFullYear() < baseYear && start.getUTCMonth() < 6) {
      start = new Date(baseYear - 1, 6);
    }

    const startMonthsFromBase =
      (start.getUTCFullYear() - baseYear) * 12 + start.getUTCMonth() + 1;
    const endMonthsFromBase =
      (end.getUTCFullYear() - baseYear) * 12 + end.getUTCMonth() + 1;
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

  function addHoverEffect(event) {
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
  }

  timelineEvents.forEach(calculatePosition);
  timelineEvents.forEach(addHoverEffect);
  endMonth = endMonth + 2;

  function appendStartDashedLineSegment(noOfMonths) {
    const dashedLineSegment = document.createElement("div");
    dashedLineSegment.className = "timeline-line dotted";
    dashedLineSegment.style.top = topOffset - 7 + "px";
    dashedLineSegment.style.height = noOfMonths * pixelsPerMonth + "px";
    timelineContainer.appendChild(dashedLineSegment);
  }

  function appendYearlyLineSegment(yearOffset) {
    const lineSegment = document.createElement("div");
    lineSegment.className = "timeline-line";
    lineSegment.style.top = yearOffset + topOffset + 67 + "px";
    lineSegment.style.height = 12 * pixelsPerMonth - 14 + "px";
    timelineContainer.appendChild(lineSegment);
  }

  function appendEndDashedLineSegment(noOfMonths, yearOffset) {
    const dashedLineSegment = document.createElement("div");
    dashedLineSegment.className = "timeline-line dotted";
    dashedLineSegment.style.top = yearOffset + topOffset + 67 + "px";
    dashedLineSegment.style.height = noOfMonths * pixelsPerMonth - 14 + "px";
    timelineContainer.appendChild(dashedLineSegment);
  }

  function appendYearMarker(year, yearOffset) {
    const yearMarker = document.createElement("div");
    yearMarker.className = "year-marker";
    yearMarker.textContent = year;
    yearMarker.style.top = yearOffset + topOffset + 60 + "px";
    timelineContainer.appendChild(yearMarker);
  }

  appendStartDashedLineSegment(6);
  for (let year = baseYear; year <= endYear; year++) {
    const yearOffset = (year - baseYear) * 12 * pixelsPerMonth;
    appendYearMarker(year, yearOffset);
    if (year === endYear) {
      appendEndDashedLineSegment(endMonth + 1, yearOffset);
    } else {
      appendYearlyLineSegment(yearOffset);
    }
  }

  timelineContainer.style.height =
    ((endYear - baseYear) * 12 + endMonth + 1) * pixelsPerMonth +
    topOffset +
    60 +
    "px";
});
