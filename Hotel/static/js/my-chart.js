//function drawCateStats(labels, data) {
//   const ctx = document.getElementById('cateStats');
//
// new Chart(ctx, {
//   type: 'pie',
//   data: {
//     labels: labels,
//     datasets: [{
//       label: 'Số lượng',
//       data: data,
//       borderWidth: 1
//     }]
//   },
//   options: {
//     scales: {
//       y: {
//         beginAtZero: true
//       }
//     }
//   }
// });
//}

function drawRevenueStats(labels, data){
   const ctx = document.getElementById('revenueStats');

 new Chart(ctx, {
   type: 'bar',
   data: {
     labels: labels,
     datasets: [{
       label: 'Doanh thu',
       data: data,
       borderWidth: 1,
       backgroundColor:['red', 'green', 'blue', 'yellow']
     }]
   },
   options: {
     scales: {
       y: {
         beginAtZero: true
       }
     }
   }
 });
}
