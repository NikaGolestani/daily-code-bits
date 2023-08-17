let list = document.getElementById("table");
let addBtn = document.getElementById("addbtn");
let btns;
let newelname;
let submitbtn;
let neweldate;
let addform = document.getElementById("addform");
addBtn.addEventListener("click", genform);
function genform() {
  addform.innerHTML = ` <label>Task</label>
  <input type="text" id="task" value='Task'><br><br>
  <label>Deadline</label>
  <input type="date" id="dline">
  <br>
  <input type='submit' id ='submitbtn' value="add"> `;

  handleform();
}
function handleform() {
  submitbtn = document.getElementById("submitbtn");
  newelname = document.getElementById("task");
  neweldate = document.getElementById("dline");
  submitbtn.addEventListener("click", handlesub);
}
function handlesub(event) {
  event.preventDefault();
  const newListItem = document.createElement("tr");
  newListItem.innerHTML = ` <td>
  ${newelname.value}
</td>
  <td>
  ${neweldate.value}
</td>
<td>
  <button name="done" class="done btns">d</button>
</td>
<td>
    <button name="fail" class="fail btns">f</button>
</td>
<td>
    <button name="del" class="del btns">🧺</button>
</td>`;
  list.appendChild(newListItem);
  addform.innerHTML = "";
  btns = document.querySelectorAll(".btns");
  btns.forEach(function (item) {
    item.addEventListener("click", function (event) {
      event.target.parentElement.parentElement.classList = `${item.name}task hide`;
    });
  });
}
