%define packname  DynDoc

Summary:	Functions for dynamic documents
Name:		R-%{packname}
Version:	1.40.0
Release:	2
License:	Artistic 2.0
Group:		X11/Applications
Source0:	http://www.bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	2a474f56576857f4cac8d85b8c3c2abd
URL:		http://bioconductor.org/packages/release/bioc/html/DynDoc.html
BuildRequires:	R
BuildRequires:	texlive-latex
Requires:	R
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of functions to create and interact with dynamic documents and
vignettes.

%prep
%setup -c -q -n %{packname}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

R CMD INSTALL %{packname} -l $RPM_BUILD_ROOT%{_libdir}/R/library

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/html
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
