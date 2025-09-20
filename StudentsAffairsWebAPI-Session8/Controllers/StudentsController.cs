//EntityFramework8 ORM object relational mapper =>
//DDL(Create table, Alter view, drop table),
//DML(Insert,Select,Update,Delete),
//DCL(Grant Update on table students to wael,revoke)

namespace StudentsAffairsWebAPI;

[Route("api/[controller]")]
[ApiController]
public class StudentsController : BaseController<Student>
{
    Student student = new();
    const int maxStudentsCount = 15;
    private readonly StudentsAffairsDbContext _studentsAffairsDbContext;
    public StudentsController(StudentsAffairsDbContext studentsAffairsDbContext) : base(studentsAffairsDbContext)
    {
        _studentsAffairsDbContext = studentsAffairsDbContext;

        if (_studentsAffairsDbContext.Students is null || !_studentsAffairsDbContext.Students.Any())
            FillStudents(maxStudentsCount);
    }
    public void FillStudents(int desiredCount)
    {
        for (int i = 1; i <= desiredCount; i++)
        {
            Student student = new() { Id = i, Name = $"Student{i}", Age = Convert.ToByte(i + 30), Mobile = $"012784512{i}" };
            _studentsAffairsDbContext.Students.Add(student);
        }

        _studentsAffairsDbContext.SaveChanges();
    }

    [HttpPost("SeedNormal/{count}")]
    public async Task<IActionResult> SeedNormal(int count)
    {
        await FillNormal(count);
        return Ok("Normal fill done");
    }

    [HttpPost("SeedBulk/{count}")]
    public async Task<IActionResult> SeedBulk(int count)
    {
        await FillBulk(count);
        return Ok("Bulk fill done");
    }
}
