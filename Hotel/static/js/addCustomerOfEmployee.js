listCus = [];
function addCusOfEmloyee() {

    e_name = document.getElementById('e_name')
    e_CCCD = document.getElementById('e_CCCD')
    e_address = document.getElementById('e_address')
    e_select_LoaiKhach = document.getElementById('e_select_LoaiKhach')
    e_ngayNhanPhong = document.getElementById('e_ngayNhanPhong')
    e_ngayTraPhong = document.getElementById('e_ngayTraPhong')

    timeBook = document.getElementById('timeBook')
    e_table = document.getElementById('e_table')


    if (e_name.value != '' && e_CCCD.value != '' && e_address.value != '' && e_select_LoaiKhach.value != '') {
        listCus.push({
            "e_name": e_name.value,
            "e_CCCD": e_CCCD.value,
            "e_address": e_address.value,
            "e_select_LoaiKhach": e_select_LoaiKhach.value,
            "e_ngayNhanPhong": e_ngayNhanPhong.value,
            "e_ngayTraPhong": e_ngayTraPhong.value

        })
    }


    e_name=''
    e_CCCD=''
    e_address=''
    e_select_LoaiKhach=''
    e_ngayNhanPhong=''
    e_ngayTraPhong=''
    e_table.innerHTML=''
    for (let i = 0; i < listCus.length; i++) {
        e_table.innerHTML += `<tr>
                        <td>${ i+1 }</td>
                        <td>${listCus[i].e_name}</td>
                        <td>${listCus[i].e_CCCD}</td>
                        <td>${listCus[i].e_address}</td>
                        <td>${listCus[i].e_select_LoaiKhach}</td>
                        <td><button class="btn btn-danger" type="button" onclick="deleteRowE(this)">X</button></td>
                    </tr>`
    }

    timeBook.innerHTML=''
     for (let i = 0; i < listCus.length; i++) {
        timeBook.innerHTML += `<td colspan="3">Ngày nhận phòng: ${listCus[i].e_ngayNhanPhong}</td>
                    <td colspan="2">Ngày trả phòng: ${listCus[i].e_ngayTraPhong}</td>`
    }
}




function deleteRowE(r) {
  var i = r.parentNode.parentNode.parentNode.rowIndex;
  if (confirm("Bạn có chắc muốn xóa!") == true) {
        document.getElementById("e_table").deleteRow(i-1);
  }
}