document.querySelector("#like").addEventListener("click", (e) => {
  // e.target : 실제 이벤트 대상 => span
  //e.currentTarget : 이벤트 대상 부모

  // post id 가져오기

  const postId = e.currentTarget.dataset.post;

  fetch(`/blog/post/like/${postId}`)
    .then((response) => response.json())
    .then((data) => {
      console.log(data);

      // 좋아요 수 : data.likes
      // 좋아요 표시 여부 : data.is_liked

      if (data.is_liked) {
        document.querySelector(".like").classList.add("show");
        document.querySelector(".dislike").classList.remove("show");
      } else {
        document.querySelector(".like").classList.remove("show");
        document.querySelector(".dislike").classList.add("show");
      }

      document.querySelector(".like-total").innerHTML = "좋아요" + data.likes + "개";
    });
});
