# Finding the Intersection of Two Polygons

Intersecting two polygons may seem easy, but it is actually quite a loaded question. There are some algorithms for this purpose, but personally I use Sutherland-Hodgman algorithm. It doesn't support concave polygons, but it is simple and fast.

``` csharp
using UnityEngine;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

public class SutherlandHodgman
{
    private class Edge
    {
        public readonly Vector2 From;
        public readonly Vector2 To;

        public Edge(Vector2 from, Vector2 to)
        {
            this.From = from;
            this.To = to;
        }
    }


    public static Vector2[] GetIntersectedPolygon(Vector2[] subjectPoly, Vector2[] clipPoly)
    {
        if (subjectPoly.Length < 3 || clipPoly.Length < 3)
        {
            throw new ArgumentException(string.Format("The polygons passed in must have at least 3 points: subject={0}, clip={1}", subjectPoly.Length.ToString(), clipPoly.Length.ToString()));
        }

        List<Vector2> outputList = subjectPoly.ToList();

        if (!IsClockwise(subjectPoly))
        {
            outputList.Reverse();
        }

        foreach (Edge clipEdge in IterateEdgesClockwise(clipPoly))
        {
            List<Vector2> inputList = outputList.ToList();
            outputList.Clear();

            if (inputList.Count == 0)
            {
                break;
            }

            Vector2 S = inputList[inputList.Count - 1];

            foreach (Vector2 E in inputList)
            {
                if (IsInside(clipEdge, E))
                {
                    if (!IsInside(clipEdge, S))
                    {
                        Vector2? point = GetIntersect(S, E, clipEdge.From, clipEdge.To);

                        if (point == null)
                        {
                            throw new ApplicationException("Line segments don't intersect");
                        }
                        else
                        {
                            outputList.Add(point.Value);
                        }
                    }

                    outputList.Add(E);
                }
                else if (IsInside(clipEdge, S))
                {
                    Vector2? point = GetIntersect(S, E, clipEdge.From, clipEdge.To);

                    if (point == null)
                    {
                        throw new ApplicationException("Line segments don't intersect");
                    }
                    else
                    {
                        outputList.Add(point.Value);
                    }
                }

                S = E;
            }
        }

        return outputList.ToArray();
    }


    private static IEnumerable<Edge> IterateEdgesClockwise(Vector2[] polygon)
    {
        if (IsClockwise(polygon))
        {
            for (int cntr = 0; cntr < polygon.Length - 1; cntr++)
            {
                yield return new Edge(polygon[cntr], polygon[cntr + 1]);
            }

            yield return new Edge(polygon[polygon.Length - 1], polygon[0]);
        }
        else
        {
            for (int cntr = polygon.Length - 1; cntr > 0; cntr--)
            {
                yield return new Edge(polygon[cntr], polygon[cntr - 1]);
            }

            yield return new Edge(polygon[0], polygon[polygon.Length - 1]);
        }
    }


    private static Vector2? GetIntersect(Vector2 line1From, Vector2 line1To, Vector2 line2From, Vector2 line2To)
    {
        Vector2 direction1 = line1To - line1From;
        Vector2 direction2 = line2To - line2From;
        float dotPerp = (direction1.x * direction2.y) - (direction1.y * direction2.x);

        if (Mathf.Approximately(dotPerp, 0))
        {
            return null;
        }

        Vector2 c = line2From - line1From;
        float t = (c.x * direction2.y - c.y * direction2.x) / dotPerp;
        return line1From + (t * direction1);
    }


    private static bool IsInside(Edge edge, Vector2 test)
    {
        bool? isLeft = IsLeftOf(edge, test);
        if (isLeft == null)
        {
            return true;
        }

        return !isLeft.Value;
    }


    private static bool IsClockwise(Vector2[] polygon)
    {
        for (int cntr = 2; cntr < polygon.Length; cntr++)
        {
            bool? isLeft = IsLeftOf(new Edge(polygon[0], polygon[1]), polygon[cntr]);

            if (isLeft != null)
            {
                return !isLeft.Value;
            }
        }

        throw new ArgumentException("All the points in the polygon are colinear");
    }


    private static bool? IsLeftOf(Edge edge, Vector2 test)
    {
        Vector2 tmp1 = edge.To - edge.From;
        Vector2 tmp2 = test - edge.To;
        float x = (tmp1.x * tmp2.y) - (tmp1.y * tmp2.x);

        if (x < 0)
        {
            return false;
        }
        else if (x > 0)
        {
            return true;
        }
        else
        {
            return null;
        }
    }
}
```
