const actionForm = document.querySelector("#actionForm");

// 제목 클릭시 actionform 보내기
document.querySelector("tbody").addEventListener("click", (e) => {
  e.preventDefault();

  // 클릭된 요소가 <a> 태그인지 확인
  if (e.target.tagName === "A") {
    // href 값 가져오기
    const href = e.target.getAttribute("href");

    // actionForm의 action 변경
    actionForm.action = `/board/${href}`;

    // Form submit
    actionForm.submit();
  }
});

// 정렬 변화가 일어나면 value를 가져온 후 actionForm의 so value 변경
document.querySelector(".so").addEventListener("change", (e) => {
  actionForm.querySelector("#so").value = e.target.value;
  actionForm.submit();
});

// 페이지 나누기 클릭시 href 값 가져오기
document.querySelector(".pagination").addEventListener("click", (e) => {
  e.preventDefault();

  // 클릭된 요소가 <a> 태그인지 확인
  if (e.target.tagName === "A") {
    const href = e.target.getAttribute("href");

    // actionForm의 page value 변경
    actionForm.querySelector("#page").value = href;
    actionForm.submit();
  }
});

// 검색어(top_keyword) 가져오기
// 없는 경우 alert()
// 있는 경우 actionForm keyword value에 삽입, page value 1로 변경
document.querySelector("#btn_search").addEventListener("click", () => {
  const top_keyword = document.querySelector("#top_keyword");

  if (top_keyword.value === "") {
    alert("검색어를 입력해 주세요");
    top_keyword.focus();
    return;
  }

  actionForm.querySelector("#keyword").value = top_keyword.value;
  actionForm.querySelector("#page").value = 1;

  actionForm.submit();
});
