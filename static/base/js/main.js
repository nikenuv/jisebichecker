const chartData = {
    labels: ["Passed", "Failed"],
    data: [80, 20],
    colors: ['#52B288', '#E95551'],
};

const myChart = document.querySelector(".my-chart");
const ul = document.querySelector(".report-stats .details ul");

new Chart(myChart, {
    type: "doughnut",
    data: {
        labels: chartData.labels,
        datasets: [
            {
                label: "Report Value",
                data: chartData.data,
                backgroundColor: chartData.colors,
            },
        ],
    },
    options: {
        responsive: false, // Menonaktifkan responsif
        plugins: {
            legend: {
                display: false, // Menyembunyikan legenda
            },
        },
        animation: {
            animateRotate: false, // Menonaktifkan animasi rotasi
            animateScale: false,  // Menonaktifkan animasi scaling
        },
    },
});

const populateUl = () => {
    chartData.labels.forEach((l, i) => {
        let li = document.createElement("li");
        li.innerHTML = `<span class='indicator' style="background-color: ${chartData.colors[i]}"></span>${l}: <span class='percentage' style="font-weight: bold; color: ${chartData.colors[i]}">${chartData.data[i]}%</span>`;
        ul.appendChild(li);
    });
};

populateUl();
