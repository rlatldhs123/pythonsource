const actionForm = document.querySelector("#actionForm");

// 목록으로 클릭시  actionForm 보내기
document.querySelector("#list").addEventListener("click", (e) => {
  e.preventDefault();

  actionForm.action = e.target.getAttribute("href");

  actionForm.submit();
});

const deleteAll = document.querySelectorAll(".delete");

deleteAll.forEach((item) => {
  item.addEventListener("click", (e) => {
    e.preventDefault();
    // href 가져오기
    const href = e.target.getAttribute("href");
    if (confirm("정말로 삭제하시겠습니까?")) {
      location.href = href;
    }
  });
});
