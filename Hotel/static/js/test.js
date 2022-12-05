
ListRoomCus = [];

function addRooms() {
    select_loaiPhong = document.getElementById('select_loaiPhong')
    soLuongKhach = document.getElementById('soLuongKhach')
    ngayNhanPhong = document.getElementById('ngayNhanPhong')
    ngayTraPhong = document.getElementById('ngayTraPhong')
    table = document.getElementById('table')



    if (select_loaiPhong.value == 1) {
         lp = 3000000
    } else if (select_loaiPhong.value == 2) {
        lp = 4000000
    } else {
        lp = 5000000
    }

    priceRoom = lp.toLocaleString('vi', {style : 'currency', currency : 'VND'})


    if (select_loaiPhong.value != '' && ngayNhanPhong.value != '' && ngayTraPhong.value != '') {
        ListRoomCus.push({
            "select_loaiPhong": select_loaiPhong.options[select_loaiPhong.selectedIndex].text,
            "ngayNhanPhong": ngayNhanPhong.value,
            "ngayTraPhong": ngayTraPhong.value,
            "priceRoom": priceRoom
        })
    }



    table.innerHTML = ''
    for (let i = 0; i < ListRoomCus.length; i++){
        table.innerHTML += `<tr>
                        <td>${ i+1 }</td>
                        <td>${ListRoomCus[i].select_loaiPhong}</td>
                        <td>${ListRoomCus[i].priceRoom}</td>
                        <td>${ListRoomCus[i].ngayNhanPhong}</td>
                        <td>${ListRoomCus[i].ngayTraPhong}</td>
                        <td><button class="btn btn-danger" type="button" onclick="deleteRow1(this)">X</button></td>
                    </tr>`
    }


}

ListAddCus = [];

function addCus() {
    name1 = document.getElementById('name1')
    phone = document.getElementById('phone')
    CCCD = document.getElementById('CCCD')
    address = document.getElementById('address')
    select_LoaiKhach = document.getElementById('select_LoaiKhach')
    btn_AddCus = document.getElementById('btn_AddCus')
    soluong = document.getElementById('soluong')
    ngayNhanPhong = document.getElementById('ngayNhanPhong')
    ngayTraPhong = document.getElementById('ngayTraPhong')


    table1 = document.getElementById('table1')
    table2 = document.getElementById('table2')


    if (name1.value != '' && phone.value != '' && CCCD.value != '' && address.value != '' && select_LoaiKhach.value != '') {
        ListAddCus.push({
            "name1": name1.value,
            "phone": phone.value,
            "CCCD": CCCD.value,
            "address": address.value,
            "select_LoaiKhach": select_LoaiKhach.options[select_LoaiKhach.selectedIndex].text,
            "select_LoaiKhach_id": select_LoaiKhach.value,
            "ngayNhanPhong": ngayNhanPhong.value,
            "ngayTraPhong": ngayTraPhong.value

        })
    }


    table1.innerHTML = ''
    for (let i = 0; i < ListAddCus.length; i++){
        table1.innerHTML += `<tr>
                        <td>${ i+1 }</td>
                        <td>${ListAddCus[i].name1}</td>
                        <td>${ListAddCus[i].phone}</td>
                        <td>${ListAddCus[i].CCCD}</td>
                        <td>${ListAddCus[i].address}</td>
                        <td>${ListAddCus[i].select_LoaiKhach}</td>
                        <td style="visibility: hidden;">${ListAddCus[i].select_LoaiKhach_id}</td>
                        <td><button class="btn btn-danger" type="button" onclick="deleteRow2(this)">X</button></td>
                    </tr>`
    }



    if (soluong.value == ListAddCus.length) {
        btn_AddCus.setAttribute('disabled', '');
    }


}





function deleteRow1(r) {
  var i = r.parentNode.parentNode.parentNode.rowIndex;
  if (confirm("Bạn có chắc muốn xóa!") == true) {
        document.getElementById("table").deleteRow(i-1);
        document.getElementById("table1").deleteRow(i-1);
  }
}

function deleteRow2(r) {
  var i = r.parentNode.parentNode.parentNode.rowIndex;
  if (confirm("Bạn có chắc muốn xóa!") == true) {
        document.getElementById("table1").deleteRow(i-1);
  }
}

